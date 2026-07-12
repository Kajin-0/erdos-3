#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>

using namespace std;

namespace {
constexpr long long L8 = 8388608LL;
constexpr long long L10 = 536870912LL;
constexpr long long D = 262143LL;  // 2^18-1
constexpr uint64_t S8_FNV = 0x023db79dd7cbf62bULL;
constexpr uint64_t S10_FNV = 0x405b941a1f8b2580ULL;
constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;

vector<long long> unique_sorted(vector<long long> values) {
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    return values;
}

vector<long long> raw(const vector<long long>& state, long long separation) {
    vector<long long> result;
    result.reserve(3 * (state.size() + 1));
    for (int layer = 0; layer < 3; ++layer) result.push_back(layer * separation);
    for (long long value : state) {
        for (int layer = 0; layer < 3; ++layer) {
            result.push_back(value + layer * separation);
        }
    }
    return unique_sorted(move(result));
}

vector<long long> translate(const vector<long long>& values, long long offset) {
    vector<long long> result;
    result.reserve(values.size());
    for (long long value : values) result.push_back(value + offset);
    return result;
}

vector<long long> build_s8() {
    const vector<long long> H = {0,1,2,16,17,18,21,22,23,26,27,28};
    const vector<long long> scales = {64,256,2048,8192,32768};
    const vector<long long> separations = {61,303,1597,8195};
    vector<long long> state;
    for (long long value : H) state.push_back(64 + value);
    state = unique_sorted(move(state));
    for (int index = 0; index < 4; ++index) {
        state = translate(raw(state, separations[index]), scales[index + 1]);
    }
    state = translate(raw(state, 93476), 262144);
    state = translate(raw(state, 230164), 1048576);
    state = translate(raw(state, 2097164), L8);
    return state;
}

vector<long long> build_s10() {
    auto state = build_s8();
    state = translate(raw(state, 16777217), 67108864);
    state = translate(raw(state, 134217729), L10);
    return state;
}

uint64_t fnv_hash(const vector<long long>& values) {
    uint64_t hash = FNV_OFFSET;
    for (long long value : values) {
        const string token = to_string(value) + ",";
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }
    return hash;
}

inline void set_bit(vector<uint64_t>& bits, long long index) {
    bits[index >> 6] |= 1ULL << (index & 63);
}

inline bool get_bit(const vector<uint64_t>& bits, long long index) {
    return (bits[index >> 6] >> (index & 63)) & 1ULL;
}

vector<long long> completion_coordinates(const vector<long long>& base, int threads) {
    const int maximum = static_cast<int>(base.back());
    const int offset = maximum;
    const int range = 3 * maximum + 1;
    vector<unsigned char> present(maximum + 1);
    for (long long value : base) present[static_cast<int>(value)] = 1;

    const size_t words = (range + 63LL) / 64;
    vector<vector<uint64_t>> local(threads, vector<uint64_t>(words));
#pragma omp parallel num_threads(threads)
    {
        const int thread = omp_get_thread_num();
        auto& bits = local[thread];
#pragma omp for schedule(dynamic,4)
        for (int first = 0; first < static_cast<int>(base.size()); ++first) {
            const int a = static_cast<int>(base[first]);
            for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
                const int b = static_cast<int>(base[second]);
                const int left = 2 * a - b;
                const int right = 2 * b - a;
                if (left >= 0 && present[left]) {
                    set_bit(bits, static_cast<long long>(right) + offset);
                }
                if (right <= maximum && present[right]) {
                    set_bit(bits, static_cast<long long>(left) + offset);
                }
            }
        }
    }

    vector<uint64_t> all(words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < words; ++word) all[word] |= bits[word];
    }

    vector<long long> result;
    for (int index = 0; index < range; ++index) {
        if (get_bit(all, index)) result.push_back(static_cast<long long>(index) - offset);
    }
    return result;
}

int v2(long long value) {
    if (value <= 0) throw invalid_argument("v2 requires a positive integer");
    return __builtin_ctzll(static_cast<unsigned long long>(value));
}
}  // namespace

int main() {
    const vector<long long> s8 = build_s8();
    if (s8.size() != 29523 || s8.front() != L8 || s8.back() != 14604604 ||
        fnv_hash(s8) != S8_FNV) {
        throw runtime_error("S8 mismatch");
    }
    if (!(s8.back() < 7 * L8 / 4)) throw runtime_error("S8 top bound failed");
    if (s8[1] - L8 != L8 / 8) throw runtime_error("S8 lower gap failed");

    vector<long long> base = {0};
    base.insert(base.end(), s8.begin(), s8.end());
    const vector<long long> completions = completion_coordinates(base, 8);
    if (completions.size() != 2772873 || completions.front() != 6291444 ||
        completions.back() != 17038008) {
        throw runtime_error("completion certificate mismatch");
    }

    const long long seed_target = 2 * L8 + D;
    if (binary_search(completions.begin(), completions.end(), seed_target)) {
        throw runtime_error("seed target is a completion");
    }
    if (!(seed_target > completions.back())) {
        throw runtime_error("seed target is not beyond the completion maximum");
    }

    const vector<long long> s10 = build_s10();
    if (s10.size() != 265719 || s10.front() != L10 || s10.back() != 920574272 ||
        fnv_hash(s10) != S10_FNV) {
        throw runtime_error("S10 mismatch");
    }
    if (s10[1] - L10 != L10 / 8) throw runtime_error("S10 lower gap failed");
    if (!(s10.back() < 7 * L10 / 4)) throw runtime_error("S10 top bound failed");

    long long cumulative = 6;  // 3*(k8+k9), with k8=k9=1.
    long long scale = L10;
    long long cardinality = 265719;
    long long persistence = 1024;
    long long offset = cumulative + D;
    if (offset != 262149 || offset - cumulative != D) {
        throw runtime_error("initial tail offset mismatch");
    }

    for (int generation = 0; generation < 10; ++generation) {
        if (v2(offset) != 2 * generation) {
            throw runtime_error("two-adic orientation mismatch");
        }
        if (!(offset * 32 < scale)) throw runtime_error("offset/scale bound failed");
        if (offset - cumulative != D) {
            throw runtime_error("completion descent invariant failed");
        }
        const long long next_cumulative = cumulative + 3 * offset;
        const long long next_offset = 4 * offset;
        if (next_offset - next_cumulative != D) {
            throw runtime_error("tail recurrence failed");
        }
        scale *= 8;
        cardinality = 3 * (cardinality + 1);
        persistence *= 2;
        cumulative = next_cumulative;
        offset = next_offset;
    }

    cout << "verified: S8 completion count=2772873 and maximum=17038008\n";
    cout << "verified: seed target 2L8+D=17039359 is beyond every S8 3-AP completion\n";
    cout << "verified: recorded S10 hash and geometry\n";
    cout << "tail_D=262143\n";
    cout << "tail_k10=262149\n";
    cout << "tail_rule=k_(h+1)=4*k_h\n";
    cout << "tail_separation=2*L_h+k_h\n";
    cout << "verified_generations=10\n";
    cout << "weighted_tail_sum_from_S10=(3^12-1)/2^18=33215/16384\n";
    return 0;
}
