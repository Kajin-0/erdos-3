#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace {
constexpr int R9 = 134217729;
constexpr int L10 = 536870912;
constexpr int MAX_R4 = 613454687;
constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;
constexpr uint64_t EXPECTED_RESIDUAL_FNV = 0x843f253a7c74453cULL;

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

long long popcount(const vector<uint64_t>& bits) {
    long long count = 0;
    for (uint64_t word : bits) count += __builtin_popcountll(word);
    return count;
}

pair<long long, vector<uint64_t>> load_bits(const string& path) {
    FILE* file = fopen(path.c_str(), "rb");
    if (!file) throw runtime_error("cannot open bitset: " + path);
    long long low;
    uint64_t words;
    if (fread(&low, 8, 1, file) != 1 || fread(&words, 8, 1, file) != 1) {
        throw runtime_error("invalid bitset header");
    }
    vector<uint64_t> bits(words);
    if (fread(bits.data(), 8, words, file) != words) {
        throw runtime_error("truncated bitset");
    }
    fclose(file);
    return {low, move(bits)};
}

vector<int> read_list(const string& path) {
    FILE* file = fopen(path.c_str(), "r");
    if (!file) throw runtime_error("cannot open list: " + path);
    vector<int> values;
    int value;
    while (fscanf(file, "%d", &value) == 1) values.push_back(value);
    fclose(file);
    return values;
}

void write_list(const string& path, const vector<int>& values) {
    FILE* file = fopen(path.c_str(), "w");
    if (!file) throw runtime_error("cannot write list: " + path);
    for (int value : values) fprintf(file, "%d\n", value);
    fclose(file);
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
}  // namespace

int main(int argc, char** argv) {
    if (argc != 5) {
        cerr << "usage: verify_depth10_factor4_mixed_completion "
             << "S9_COMPLETIONS_BIN S9_COMPLETION_DIFFERENCES_BIN "
             << "INPUT_RESIDUAL OUTPUT_RESIDUAL\n";
        return 2;
    }

    const auto [completion_low, completions] = load_bits(argv[1]);
    const auto [difference_low, differences] = load_bits(argv[2]);
    const vector<int> input = read_list(argv[3]);

    if (completion_low != -115267902LL || popcount(completions) != 13923661) {
        throw runtime_error("S9 completion bitset mismatch");
    }
    if (difference_low != 0 || popcount(differences) != 71129286) {
        throw runtime_error("S9 completion-difference support mismatch");
    }
    if (input.size() != 1866 || input.front() != 97530521 ||
        input.back() != 613340173 || fnv_values(input) != 0xf728ae4689a0fe2aULL) {
        throw runtime_error("input residual mismatch");
    }

    const long long support_limit = 3LL * MAX_R4;
    vector<uint64_t> lifted((support_limit + 64) / 64);

    // Same-copy and ordinary inter-copy completion witnesses use layer gaps
    // 0,1,2. A base 3-AP placed in raw layers 0,1,2 has its missing right
    // completion in layer 3 (and the reflected left completion in layer -1),
    // producing the additional mixed gap 3.
    for (size_t word = 0; word < differences.size(); ++word) {
        uint64_t active = differences[word];
        while (active) {
            const int offset = __builtin_ctzll(active);
            const long long difference = static_cast<long long>(word) * 64 + offset;
            for (int layer_gap = 0; layer_gap <= 3; ++layer_gap) {
                set_bit(lifted, llabs(difference + 1LL * layer_gap * R9));
                set_bit(lifted, llabs(difference - 1LL * layer_gap * R9));
            }
            active &= active - 1;
        }
    }

    // Embedded completion coordinates may also be paired with the global
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

    if (popcount(lifted) != 475807917) {
        throw runtime_error("mixed completion support mismatch");
    }

    vector<int> remaining;
    for (int separation : input) {
        if (!get_bit(lifted, separation) &&
            !get_bit(lifted, 2LL * separation) &&
            !get_bit(lifted, 3LL * separation)) {
            remaining.push_back(separation);
        }
    }

    if (remaining.size() != 893 || remaining.front() != 97530521 ||
        remaining.back() != 613340173 ||
        fnv_values(remaining) != EXPECTED_RESIDUAL_FNV) {
        throw runtime_error("mixed completion residual mismatch");
    }

    write_list(argv[4], remaining);
    cout << "verified: mixed layer-012 completion lift\n";
    cout << "lifted_support_size=475807917\n";
    cout << "input_candidates=1866\n";
    cout << "mixed_completion_covered=973\n";
    cout << "remaining_candidates=893\n";
    cout << "residual_fnv64=843f253a7c74453c\n";
    return 0;
}
