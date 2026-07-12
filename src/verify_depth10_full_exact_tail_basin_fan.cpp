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
constexpr int K_MIN = 4;
constexpr int K_MAX = 1048579;
constexpr long long EXPECTED_COMPLETIONS = 2772873;
constexpr long long EXPECTED_SPONSOR = 699051;
constexpr long long EXPECTED_BLOCKED = 54999;
constexpr long long EXPECTED_VALID = 644052;
constexpr uint64_t EXPECTED_FNV = 0x5e1b143b6a59b345ULL;
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
    return (bits[index >> 6] >> (index & 63)) & 1ULL;
}
}  // namespace

int main(int argc, char** argv) {
    const char* dump_path = argc >= 2 ? argv[1] : nullptr;

    const vector<int> s8 = build_s8();
    vector<int> base = {0};
    base.insert(base.end(), s8.begin(), s8.end());
    if (base.size() != 29524 || base.front() != 0 || base.back() != 14604604) {
        throw runtime_error("S8 anchor geometry mismatch");
    }

    const int maximum = base.back();
    const int offset = maximum;
    const int range = 3 * maximum + 1;
    vector<unsigned char> present(maximum + 1);
    for (int value : base) present[value] = 1;

    const int thread_count = 8;
    const size_t words = (range + 63LL) / 64;
    vector<vector<uint64_t>> local(
        thread_count,
        vector<uint64_t>(words)
    );

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
                if (left >= 0 && present[left]) {
                    set_bit(bits, right + offset);
                }
                if (right <= maximum && present[right]) {
                    set_bit(bits, left + offset);
                }
            }
        }
    }

    vector<uint64_t> completions(words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < words; ++word) {
            completions[word] |= bits[word];
        }
    }

    long long completion_count = 0;
    for (uint64_t word : completions) {
        completion_count += __builtin_popcountll(word);
    }
    if (completion_count != EXPECTED_COMPLETIONS) {
        throw runtime_error("S8 completion count mismatch");
    }

    FILE* dump = dump_path ? fopen(dump_path, "wb") : nullptr;
    if (dump_path && !dump) throw runtime_error("could not open dump path");

    long long sponsor_count = 0;
    long long blocked_count = 0;
    long long valid_count = 0;
    vector<long long> classes(32);
    uint64_t hash = FNV_OFFSET;
    int first_valid = -1;
    int last_valid = -1;

    for (int k = K_MIN; k <= K_MAX; ++k) {
        if (v2(k) % 2 != 0) continue;
        ++sponsor_count;

        // Two completion descents subtract 3+3 from the S10 offset.
        const long long seed_completion = 2LL * L8 + (k - 6);
        if (get_bit(completions, seed_completion + offset)) {
            ++blocked_count;
            continue;
        }

        ++valid_count;
        ++classes[v2(k)];
        if (first_valid < 0) first_valid = k;
        last_valid = k;

        const string token = to_string(k) + ",";
        if (dump) fwrite(token.data(), 1, token.size(), dump);
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }

    if (dump) fclose(dump);

    if (sponsor_count != EXPECTED_SPONSOR ||
        blocked_count != EXPECTED_BLOCKED ||
        valid_count != EXPECTED_VALID ||
        hash != EXPECTED_FNV ||
        first_valid != 4 ||
        last_valid != 1048579) {
        throw runtime_error("full basin fan certificate mismatch");
    }

    const vector<long long> expected_classes = {
        483016,0,120732,0,30191,0,7584,0,1892,0,472,0,
        123,0,31,0,8,0,2,0,1
    };
    for (size_t index = 0; index < expected_classes.size(); ++index) {
        if (classes[index] != expected_classes[index]) {
            throw runtime_error("two-adic class mismatch");
        }
    }

    cout << "verified: full two-step-descent basin fan at S10\n";
    cout << "completion_count_S8=2772873\n";
    cout << "k_min=4\n";
    cout << "k_max=1048579\n";
    cout << "sponsor_compatible=699051\n";
    cout << "blocked_by_seed_completion=54999\n";
    cout << "valid_basin_offsets=644052\n";
    cout << "valid_offset_fnv64=5e1b143b6a59b345\n";
    cout << "valid_offset_sha256=22daeb2366e5e3324b7e835c61adb34f8e08c0ae203b86420c941f53991069b4\n";
    cout << "terminal_charge=33215/16384\n";
    return 0;
}
