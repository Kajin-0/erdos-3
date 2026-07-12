#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>

using namespace std;

namespace {
constexpr int L8 = 8388608;
constexpr int L9 = 67108864;
constexpr int L10 = 536870912;
constexpr int R8 = 16777217;
constexpr int R9 = 134217729;
constexpr int S10_MAX = 920574272;
constexpr int MAX_R2 = 76583775;
constexpr int MAX_R4 = 613454687;
constexpr uint64_t S10_FNV = 0x405b941a1f8b2580ULL;
constexpr uint64_t FACTOR2_DOMAIN_FNV = 0x59cfbc6761c6224dULL;
constexpr uint64_t FACTOR4_DOMAIN_FNV = 0xae1d9e1ec77b2dfbULL;
constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;

vector<int> unique_sorted(vector<int> values) {
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    return values;
}

vector<int> raw(const vector<int>& state, int separation) {
    vector<int> result;
    result.reserve(3 * (state.size() + 1));
    for (int layer = 0; layer < 3; ++layer) result.push_back(layer * separation);
    for (int value : state) {
        for (int layer = 0; layer < 3; ++layer) {
            result.push_back(value + layer * separation);
        }
    }
    return unique_sorted(move(result));
}

vector<int> translate(const vector<int>& values, int offset) {
    vector<int> result;
    result.reserve(values.size());
    for (int value : values) result.push_back(value + offset);
    return result;
}

vector<int> build_s8() {
    const vector<int> H = {0,1,2,16,17,18,21,22,23,26,27,28};
    const vector<int> scales = {64,256,2048,8192,32768};
    const vector<int> separations = {61,303,1597,8195};
    vector<int> state;
    for (int value : H) state.push_back(64 + value);
    state = unique_sorted(move(state));
    for (int index = 0; index < 4; ++index) {
        state = translate(raw(state, separations[index]), scales[index + 1]);
    }
    state = translate(raw(state, 93476), 262144);
    state = translate(raw(state, 230164), 1048576);
    state = translate(raw(state, 2097164), L8);
    return state;
}

int v2(int value) {
    if (value <= 0) throw invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(value));
}

inline void set_bit(vector<uint64_t>& bits, long long value) {
    if (value > 0 && static_cast<uint64_t>(value >> 6) < bits.size()) {
        __atomic_fetch_or(
            &bits[value >> 6],
            1ULL << (value & 63),
            __ATOMIC_RELAXED
        );
    }
}

inline bool get_bit(const vector<uint64_t>& bits, long long value) {
    return value > 0 &&
        static_cast<uint64_t>(value >> 6) < bits.size() &&
        ((bits[value >> 6] >> (value & 63)) & 1ULL);
}

uint64_t fnv_values(const vector<int>& values) {
    uint64_t hash = FNV_OFFSET;
    for (int value : values) {
        const string token = to_string(value) + ",";
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }
    return hash;
}

struct DomainSummary {
    long long sponsor_count;
    long long disjoint_count;
    uint64_t disjoint_hash;
};

DomainSummary summarize_domain(
    const vector<uint64_t>& differences,
    int maximum_r
) {
    long long sponsor_count = 0;
    long long disjoint_count = 0;
    uint64_t hash = FNV_OFFSET;
    for (int separation = 1; separation <= maximum_r; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        ++sponsor_count;
        if (get_bit(differences, separation) ||
            get_bit(differences, 2LL * separation)) {
            continue;
        }
        ++disjoint_count;
        const string token = to_string(separation) + ",";
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }
    return {sponsor_count, disjoint_count, hash};
}
}  // namespace

int main() {
    const vector<int> s8 = build_s8();
    vector<int> a8 = {0};
    a8.insert(a8.end(), s8.begin(), s8.end());
    if (a8.size() != 29524) throw runtime_error("A8 size mismatch");

    const int max_a8 = a8.back();
    vector<uint64_t> differences_a8((max_a8 + 64LL) / 64);
#pragma omp parallel for schedule(dynamic,4)
    for (int first = 0; first < static_cast<int>(a8.size()); ++first) {
        for (int second = first + 1; second < static_cast<int>(a8.size()); ++second) {
            set_bit(differences_a8, a8[second] - a8[first]);
        }
    }

    const vector<int> s9 = translate(raw(s8, R8), L9);
    vector<int> a9 = {0};
    a9.insert(a9.end(), s9.begin(), s9.end());
    const int max_a9 = a9.back();
    vector<uint64_t> differences_a9((max_a9 + 64LL) / 64);

    for (int value : s9) set_bit(differences_a9, value);
    set_bit(differences_a9, R8);
    set_bit(differences_a9, 2LL * R8);
    for (int difference = 1; difference <= max_a8; ++difference) {
        if (!get_bit(differences_a8, difference)) continue;
        set_bit(differences_a9, difference);
        set_bit(differences_a9, 1LL * R8 + difference);
        set_bit(differences_a9, llabs(1LL * R8 - difference));
        set_bit(differences_a9, 2LL * R8 + difference);
        set_bit(differences_a9, llabs(2LL * R8 - difference));
    }

    // Audit the recursive difference construction against the already certified S9 domains.
    const DomainSummary s9_factor2 = summarize_domain(differences_a9, 9474912);
    const DomainSummary s9_factor4 = summarize_domain(differences_a9, 76583776);
    if (s9_factor2.sponsor_count != 6316608 ||
        s9_factor2.disjoint_count != 2967413) {
        throw runtime_error("S9 factor-two audit mismatch");
    }
    if (s9_factor4.sponsor_count != 51055851 ||
        s9_factor4.disjoint_count != 39459384) {
        throw runtime_error("S9 factor-four audit mismatch");
    }

    const vector<int> s10 = translate(raw(s9, R9), L10);
    if (s10.size() != 265719 || s10.front() != L10 ||
        s10.back() != S10_MAX || fnv_values(s10) != S10_FNV) {
        throw runtime_error("S10 mismatch");
    }

    const long long maximum_difference = 2LL * MAX_R4;
    vector<uint64_t> differences_s10((maximum_difference + 64) / 64);

    // Differences from the anchor zero to S10.
    for (int value : s10) set_bit(differences_s10, value);

    // Differences inside the three Q9-translate layers of the raw S10 parent.
    set_bit(differences_s10, R9);
    set_bit(differences_s10, 2LL * R9);
    for (int difference = 1; difference <= max_a9; ++difference) {
        if (!get_bit(differences_a9, difference)) continue;
        set_bit(differences_s10, difference);
        set_bit(differences_s10, 1LL * R9 + difference);
        set_bit(differences_s10, llabs(1LL * R9 - difference));
        set_bit(differences_s10, 2LL * R9 + difference);
        set_bit(differences_s10, llabs(2LL * R9 - difference));
    }

    const DomainSummary factor2 = summarize_domain(differences_s10, MAX_R2);
    const DomainSummary factor4 = summarize_domain(differences_s10, MAX_R4);

    if (factor2.sponsor_count != 51055851 ||
        factor2.disjoint_count != 33026376 ||
        factor2.disjoint_hash != FACTOR2_DOMAIN_FNV) {
        throw runtime_error("S10 factor-two domain mismatch");
    }
    if (factor4.sponsor_count != 408969792 ||
        factor4.disjoint_count != 348012826 ||
        factor4.disjoint_hash != FACTOR4_DOMAIN_FNV) {
        throw runtime_error("S10 factor-four domain mismatch");
    }

    cout << "verified: recursive S10 positive-difference support\n";
    cout << "verified: S9 domain audit reproduced\n";
    cout << "factor2_max_R=76583775\n";
    cout << "factor2_sponsor_candidates=51055851\n";
    cout << "factor2_disjoint_candidates=33026376\n";
    cout << "factor2_disjoint_fnv64=59cfbc6761c6224d\n";
    cout << "factor4_max_R=613454687\n";
    cout << "factor4_sponsor_candidates=408969792\n";
    cout << "factor4_disjoint_candidates=348012826\n";
    cout << "factor4_disjoint_fnv64=ae1d9e1ec77b2dfb\n";
    return 0;
}
