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
constexpr int MAX_R4 = 613454687;
constexpr int INHERITED_MAX_R = 76583775;
constexpr uint64_t RESIDUAL_FNV = 0x00369694f2d70526ULL;
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
    if (value >= 0 && static_cast<uint64_t>(value >> 6) < bits.size()) {
        bits[value >> 6] |= 1ULL << (value & 63);
    }
}

inline bool get_bit(const vector<uint64_t>& bits, long long value) {
    return value >= 0 &&
        static_cast<uint64_t>(value >> 6) < bits.size() &&
        ((bits[value >> 6] >> (value & 63)) & 1ULL);
}

pair<long long, vector<uint64_t>> load_bits(const string& path) {
    FILE* file = fopen(path.c_str(), "rb");
    if (!file) throw runtime_error("cannot open bitset: " + path);
    long long low;
    uint64_t count;
    if (fread(&low, 8, 1, file) != 1 || fread(&count, 8, 1, file) != 1) {
        throw runtime_error("invalid bitset header");
    }
    vector<uint64_t> bits(count);
    if (fread(bits.data(), 8, count, file) != count) {
        throw runtime_error("truncated bitset");
    }
    fclose(file);
    return {low, move(bits)};
}

long long bit_count(const vector<uint64_t>& bits) {
    long long count = 0;
    for (uint64_t word : bits) count += __builtin_popcountll(word);
    return count;
}

void hash_value(uint64_t& hash, int value) {
    const string token = to_string(value) + ",";
    for (unsigned char byte : token) {
        hash ^= byte;
        hash *= FNV_PRIME;
    }
}
}  // namespace

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: verify_depth10_lifted_s9_completion "
             << "S9_COMPLETIONS_BIN S9_COMPLETION_DIFFERENCES_BIN\n";
        return 2;
    }

    const auto [completion_low, completions] = load_bits(argv[1]);
    const auto [difference_low, s9_completion_differences] = load_bits(argv[2]);

    if (completion_low != -115267902LL || bit_count(completions) != 13923661) {
        throw runtime_error("S9 completion bitset mismatch");
    }
    if (difference_low != 0 || bit_count(s9_completion_differences) != 71129286) {
        throw runtime_error("S9 completion-difference support mismatch");
    }

    const long long support_limit = 3LL * MAX_R4;
    vector<uint64_t> lifted((support_limit + 64) / 64);

    // Compare a completion in one embedded A9 copy with a base point in any
    // of the three embedded A9 copies. If d is an absolute S9
    // completion-to-base difference, the possible lifted differences are
    // |d +/- m R9| for m=0,1,2.
    for (size_t word = 0; word < s9_completion_differences.size(); ++word) {
        uint64_t active = s9_completion_differences[word];
        while (active) {
            const int offset = __builtin_ctzll(active);
            const long long difference = static_cast<long long>(word) * 64 + offset;
            for (int layer_gap = 0; layer_gap <= 2; ++layer_gap) {
                set_bit(lifted, llabs(difference + 1LL * layer_gap * R9));
                set_bit(lifted, llabs(difference - 1LL * layer_gap * R9));
            }
            active &= active - 1;
        }
    }

    // Compare an embedded completion coordinate directly with the global
    // anchor zero.
    for (size_t word = 0; word < completions.size(); ++word) {
        uint64_t active = completions[word];
        while (active) {
            const int offset = __builtin_ctzll(active);
            const long long coordinate =
                completion_low + static_cast<long long>(word) * 64 + offset;
            for (int layer = 0; layer < 3; ++layer) {
                set_bit(lifted, llabs(1LL * L10 + layer * 1LL * R9 + coordinate));
            }
            active &= active - 1;
        }
    }

    if (bit_count(lifted) != 354838701) {
        throw runtime_error("lifted completion support mismatch");
    }

    // Reconstruct the certified S10 positive-difference support.
    const vector<int> s8 = build_s8();
    vector<int> a8 = {0};
    a8.insert(a8.end(), s8.begin(), s8.end());
    const int max_a8 = a8.back();
    vector<uint64_t> differences_a8((max_a8 + 64LL) / 64);

#pragma omp parallel for schedule(dynamic,4)
    for (int first = 0; first < static_cast<int>(a8.size()); ++first) {
        for (int second = first + 1; second < static_cast<int>(a8.size()); ++second) {
            const int difference = a8[second] - a8[first];
            __atomic_fetch_or(
                &differences_a8[difference >> 6],
                1ULL << (difference & 63),
                __ATOMIC_RELAXED
            );
        }
    }

    const vector<int> s9 = translate(raw(s8, R8), L9);
    const int max_a9 = s9.back();
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

    const vector<int> s10 = translate(raw(s9, R9), L10);
    vector<uint64_t> differences_s10((2LL * MAX_R4 + 64) / 64);
    for (int value : s10) set_bit(differences_s10, value);
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

    long long sponsor_count = 0;
    long long disjoint_count = 0;
    long long completion_covered = 0;
    long long new_range_covered = 0;
    long long new_remaining = 0;
    int first_remaining = 0;
    int last_remaining = 0;
    uint64_t residual_hash = FNV_OFFSET;

    for (int separation = 1; separation <= MAX_R4; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        ++sponsor_count;
        if (get_bit(differences_s10, separation) ||
            get_bit(differences_s10, 2LL * separation)) {
            continue;
        }
        ++disjoint_count;

        const bool covered =
            get_bit(lifted, separation) ||
            get_bit(lifted, 2LL * separation) ||
            get_bit(lifted, 3LL * separation);

        if (covered) {
            ++completion_covered;
            if (separation > INHERITED_MAX_R) ++new_range_covered;
            continue;
        }

        if (separation > INHERITED_MAX_R) {
            ++new_remaining;
            if (!first_remaining) first_remaining = separation;
            last_remaining = separation;
            hash_value(residual_hash, separation);
        }
    }

    if (sponsor_count != 408969792 || disjoint_count != 348012826) {
        throw runtime_error("S10 factor-four domain mismatch");
    }
    if (completion_covered != 170164054 ||
        new_range_covered != 137142200 ||
        new_remaining != 177844250 ||
        first_remaining != 97474324 ||
        last_remaining != 613454687 ||
        residual_hash != RESIDUAL_FNV) {
        throw runtime_error("lifted completion classification mismatch");
    }

    cout << "verified: lifted S9 completion support at S10\n";
    cout << "lifted_support_size=354838701\n";
    cout << "factor4_disjoint_candidates=348012826\n";
    cout << "genuinely_new_candidates=314986450\n";
    cout << "new_range_completion_covered=137142200\n";
    cout << "new_range_remaining=177844250\n";
    cout << "first_new_remaining=97474324\n";
    cout << "last_new_remaining=613454687\n";
    cout << "new_residual_fnv64=00369694f2d70526\n";
    return 0;
}
