#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>

using namespace std;

namespace {
constexpr int L7 = 1048576;
constexpr int L8 = 8388608;
constexpr int R7 = 2097164;
constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;
constexpr uint64_t G8_FNV = 0xb5fad81d83531b77ULL;
constexpr uint64_t S8_FNV = 0x023db79dd7cbf62bULL;

int v2(int value) {
    if (value <= 0) throw invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(value));
}

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
    for (int value : values) result.push_back(offset + value);
    return result;
}

vector<int> build_s7() {
    const vector<int> H = {0,1,2,16,17,18,21,22,23,26,27,28};
    const vector<int> scales = {64,256,2048,8192,32768};
    const vector<int> separations = {61,303,1597,8195};

    vector<int> state;
    for (int value : H) state.push_back(64 + value);
    state = unique_sorted(move(state));

    for (size_t index = 0; index < separations.size(); ++index) {
        state = translate(raw(state, separations[index]), scales[index + 1]);
    }
    state = translate(raw(state, 93476), 262144);
    state = translate(raw(state, 230164), L7);
    return state;
}

uint64_t fnv_hash(const vector<int>& values) {
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

bool has_four_ap(const vector<int>& values, int ambient_limit) {
    vector<unsigned char> present(ambient_limit, 0);
    for (int value : values) present[value] = 1;

    atomic<bool> found{false};
    const int maximum = values.back();
#pragma omp parallel for schedule(dynamic,16)
    for (int i = 0; i < static_cast<int>(values.size()); ++i) {
        if (found.load(memory_order_relaxed)) continue;
        const int middle_left = values[i];
        const int upper_value = (maximum + middle_left) / 2;
        const int stop = upper_bound(
            values.begin() + i + 1,
            values.end(),
            upper_value
        ) - values.begin();
        for (int j = i + 1; j < stop; ++j) {
            const int middle_right = values[j];
            const int first = 2 * middle_left - middle_right;
            if (first < 0) continue;
            const int fourth = 2 * middle_right - middle_left;
            if (present[first] && present[fourth]) {
                found.store(true, memory_order_relaxed);
                break;
            }
        }
    }
    return found.load();
}

void verify_left_schedule(const vector<int>& state, int separation) {
    const vector<int> generated = raw(state, separation);
    unordered_set<int> working(generated.begin(), generated.end());
    vector<int> sponsors = {0};
    sponsors.insert(sponsors.end(), state.begin(), state.end());

    for (int sponsor : sponsors) {
        for (int layer = 0; layer < 3; ++layer) {
            if (!working.count(sponsor + layer * separation)) {
                throw runtime_error("infeasible left-sponsor deletion schedule");
            }
        }
        working.erase(sponsor);
    }
}
} // namespace

int main() {
    const vector<int> s7 = build_s7();
    if (s7.size() != 9840 || s7.front() != L7 || s7.back() != 2021668) {
        throw runtime_error("unexpected S7 geometry");
    }

    int first_valid = 0;
    for (int separation = 2 * L7; separation <= R7; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        const vector<int> candidate = raw(s7, separation);
        if (candidate.size() != 3 * (s7.size() + 1)) continue;
        if (candidate.back() >= L8) continue;
        if (!has_four_ap(candidate, L8)) {
            first_valid = separation;
            break;
        }
    }
    if (first_valid != R7) {
        throw runtime_error("unexpected first exact factor-eight continuation");
    }

    const vector<int> g8 = raw(s7, R7);
    if (v2(R7) != 2) throw runtime_error("wrong sponsor orientation");
    if (g8.size() != 29523 || g8.front() != 0 || g8.back() != 6215996) {
        throw runtime_error("unexpected G8 geometry");
    }
    if (has_four_ap(g8, L8)) throw runtime_error("G8 contains a four-term progression");
    if (fnv_hash(g8) != G8_FNV) throw runtime_error("G8 hash mismatch");

    verify_left_schedule(s7, R7);

    vector<int> backbone;
    for (int value : g8) {
        if (L7 <= value && value < 2 * L7) backbone.push_back(value);
    }
    if (backbone != s7) throw runtime_error("factor-eight backbone is not exact");

    const vector<int> s8 = translate(g8, L8);
    if (s8.size() != 29523 || s8.front() != L8 || s8.back() != 14604604) {
        throw runtime_error("unexpected S8 geometry");
    }
    if (fnv_hash(s8) != S8_FNV) throw runtime_error("S8 hash mismatch");

    cout << "verified: first exact factor-eight continuation R7=2097164\n";
    cout << "verified: G8 and S8 are four-term-progression-free\n";
    cout << "verified: exact backbone reproduction\n";
    cout << "scale_factors=4,8,4,4,8,4,8\n";
    cout << "state_size_S8=29523\n";
    cout << "weighted_density_S8=29523/32768\n";
    cout << "weighted_density_growth_S8_over_S5=757/896\n";
    cout << "G8_fnv64=b5fad81d83531b77\n";
    cout << "S8_fnv64=023db79dd7cbf62b\n";
    return 0;
}
