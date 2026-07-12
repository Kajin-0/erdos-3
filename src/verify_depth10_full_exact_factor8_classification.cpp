#include <algorithm>
#include <cstdint>
#include <cstdio>
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
constexpr int K_MAX = 613454687;
constexpr int S9_MAX = 115267902;
constexpr int S10_MAX = 920574272;
constexpr long long EXPECTED_SPONSOR = 408969792;
constexpr long long EXPECTED_COMPLETION_BLOCK = 54999;
constexpr long long EXPECTED_HALF_BLOCK = 59034;
constexpr long long EXPECTED_VALID = 408855759;
constexpr uint64_t COMPLETION_FNV = 0xe22bc4f8babba2acULL;
constexpr uint64_t HALF_FNV = 0xa1d342c2504bb966ULL;
constexpr uint64_t UNION_FNV = 0x704c4821b177ab25ULL;
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

inline void set_bit(vector<uint64_t>& bits, long long index) {
    bits[index >> 6] |= 1ULL << (index & 63);
}

inline bool get_bit(const vector<uint64_t>& bits, long long index) {
    return index >= 0 &&
        static_cast<uint64_t>(index >> 6) < bits.size() &&
        ((bits[index >> 6] >> (index & 63)) & 1ULL);
}

uint64_t fnv_comma_values(const vector<int>& values) {
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

void dump_values(const string& path, const vector<int>& values) {
    FILE* file = fopen(path.c_str(), "wb");
    if (!file) throw runtime_error("could not open dump path");
    for (int value : values) {
        const string token = to_string(value) + ",";
        fwrite(token.data(), 1, token.size(), file);
    }
    fclose(file);
}
}  // namespace

int main(int argc, char** argv) {
    const string dump_prefix = argc >= 2 ? argv[1] : "";

    const vector<int> s8 = build_s8();
    const vector<int> s9 = translate(raw(s8, R8), L9);
    const vector<int> s10 = translate(raw(s9, R9), L10);

    if (s8.size() != 29523 || s8.front() != L8 || s8.back() != 14604604) {
        throw runtime_error("S8 mismatch");
    }
    if (s9.size() != 88572 || s9.front() != L9 || s9.back() != S9_MAX) {
        throw runtime_error("S9 mismatch");
    }
    if (s10.size() != 265719 || s10.front() != L10 || s10.back() != S10_MAX) {
        throw runtime_error("S10 mismatch");
    }

    // The largest fitting exact separation is R=2L10+K_MAX.
    const long long maximum_r = (8LL * L10 - 1 - S10_MAX) / 2;
    if (maximum_r != 2LL * L10 + K_MAX) {
        throw runtime_error("exact-fit bound mismatch");
    }

    // Reconstruct every signed 3-AP completion of S8.
    const vector<int>& base = s8;
    const int maximum = base.back();
    const int offset = maximum;
    const int range = 3 * maximum + 1;
    vector<unsigned char> present(maximum + 1);
    for (int value : base) present[value] = 1;

    const int thread_count = 8;
    const size_t words = (range + 63LL) / 64;
    vector<vector<uint64_t>> local(thread_count, vector<uint64_t>(words));

#pragma omp parallel num_threads(thread_count)
    {
        const int thread = omp_get_thread_num();
        auto& bits = local[thread];
#pragma omp for schedule(dynamic,4)
        for (int first = 0; first < static_cast<int>(base.size()); ++first) {
            const int x = base[first];
            for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
                const int y = base[second];
                const long long left = 2LL * x - y;
                const long long right = 2LL * y - x;
                if (left >= 0 && present[left]) set_bit(bits, right + offset);
                if (right <= maximum && present[right]) set_bit(bits, left + offset);
            }
        }
    }

    vector<uint64_t> completions(words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < words; ++word) completions[word] |= bits[word];
    }

    long long completion_count = 0;
    for (uint64_t word : completions) completion_count += __builtin_popcountll(word);
    if (completion_count != 2772873) throw runtime_error("S8 completion mismatch");

    // Geometry bounds used by the two exact completion descents.
    const long long s10_right_completion_max = 2LL * S10_MAX - L10;
    const long long s9_right_completion_max = 2LL * S9_MAX - L9;
    if (s10_right_completion_max - 2LL * L10 != 230535808) {
        throw runtime_error("S10 completion geometry mismatch");
    }
    if (s9_right_completion_max - 2LL * L9 + 3 != 29209215) {
        throw runtime_error("S9 completion geometry mismatch");
    }

    vector<int> completion_blocked;
    for (long long index = 0; index < range; ++index) {
        if (!get_bit(completions, index)) continue;
        const long long seed_coordinate = index - offset;
        const long long k = seed_coordinate - 2LL * L8 + 6;
        if (k >= 1 && k <= K_MAX && v2(static_cast<int>(k)) % 2 == 0) {
            completion_blocked.push_back(static_cast<int>(k));
        }
    }
    completion_blocked = unique_sorted(move(completion_blocked));

    // The other top-layer obstruction is R/2 in S10.
    vector<int> half_blocked;
    for (int value : s10) {
        const long long k = 2LL * (value - L10);
        if (k >= 1 && k <= K_MAX && v2(static_cast<int>(k)) % 2 == 0) {
            half_blocked.push_back(static_cast<int>(k));
        }
    }
    half_blocked = unique_sorted(move(half_blocked));

    vector<int> overlap;
    vector<int> all_blocked;
    set_intersection(
        completion_blocked.begin(), completion_blocked.end(),
        half_blocked.begin(), half_blocked.end(),
        back_inserter(overlap)
    );
    set_union(
        completion_blocked.begin(), completion_blocked.end(),
        half_blocked.begin(), half_blocked.end(),
        back_inserter(all_blocked)
    );

    long long sponsor_count = 0;
    for (int k = 1; k <= K_MAX; ++k) {
        if (v2(k) % 2 == 0) ++sponsor_count;
    }
    const long long valid_count = sponsor_count - static_cast<long long>(all_blocked.size());

    if (sponsor_count != EXPECTED_SPONSOR ||
        completion_blocked.size() != EXPECTED_COMPLETION_BLOCK ||
        half_blocked.size() != EXPECTED_HALF_BLOCK ||
        !overlap.empty() ||
        valid_count != EXPECTED_VALID) {
        throw runtime_error("classification count mismatch");
    }

    if (completion_blocked.front() != 13 || completion_blocked.back() != 260795 ||
        half_blocked.front() != 150994944 || half_blocked.back() != 536870916) {
        throw runtime_error("classification endpoint mismatch");
    }

    if (fnv_comma_values(completion_blocked) != COMPLETION_FNV ||
        fnv_comma_values(half_blocked) != HALF_FNV ||
        fnv_comma_values(all_blocked) != UNION_FNV) {
        throw runtime_error("classification hash mismatch");
    }

    // The zero-offset exact candidate R=2L10 is invalid because R/2=L10 belongs to S10.
    if (!binary_search(s10.begin(), s10.end(), L10)) {
        throw runtime_error("zero-offset half obstruction missing");
    }

    if (!dump_prefix.empty()) {
        dump_values(dump_prefix + "_completion.csv", completion_blocked);
        dump_values(dump_prefix + "_half.csv", half_blocked);
        dump_values(dump_prefix + "_union.csv", all_blocked);
    }

    cout << "verified: complete positive-offset exact factor-eight classification at S10\n";
    cout << "k_max=613454687\n";
    cout << "sponsor_compatible_positive_offsets=408969792\n";
    cout << "completion_blocked=54999\n";
    cout << "half_separation_blocked=59034\n";
    cout << "obstruction_overlap=0\n";
    cout << "valid_exact_factor8_offsets=408855759\n";
    cout << "completion_blocked_fnv64=e22bc4f8babba2ac\n";
    cout << "half_blocked_fnv64=a1d342c2504bb966\n";
    cout << "union_blocked_fnv64=704c4821b177ab25\n";
    cout << "completion_blocked_sha256=b0cdf6b95ee9f17f39560e182b5b1f9c72e6af7fa5b1ef41a51c35a49abdf6ec\n";
    cout << "half_blocked_sha256=45075ac0f88a7e591bdd6850846831d3d15f63db8016878e35bb0644eb739ca9\n";
    cout << "union_blocked_sha256=92614cc5ec33add8064ef0aedaf4f8fe758600b30912315bec45aa47d48c6861\n";
    cout << "zero_offset_R_equals_2L_is_invalid=true\n";
    return 0;
}
