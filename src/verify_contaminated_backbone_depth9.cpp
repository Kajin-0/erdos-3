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
constexpr int L8 = 8388608;
constexpr int L9 = 67108864;
constexpr int R8 = 16777217;
constexpr uint64_t G9_FNV = 0xa323906d13700252ULL;
constexpr uint64_t S9_FNV = 0x5005dc89644a7b80ULL;
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

pair<bool,array<int,4>> first_four_ap(const vector<int>& values, int ambient_limit) {
    vector<unsigned char> present(ambient_limit);
    for (int value : values) present[value] = 1;
    atomic<bool> found{false};
    array<int,4> witness = {0,0,0,0};
    const int maximum = values.back();
#pragma omp parallel for schedule(dynamic,8)
    for (int index = 0; index < static_cast<int>(values.size()); ++index) {
        if (found.load(memory_order_relaxed)) continue;
        const int middle_left = values[index];
        const int stop = upper_bound(
            values.begin() + index + 1,
            values.end(),
            (maximum + middle_left) / 2
        ) - values.begin();
        for (int second = index + 1; second < stop; ++second) {
            const int middle_right = values[second];
            const int first = 2 * middle_left - middle_right;
            if (first < 0) continue;
            const int fourth = 2 * middle_right - middle_left;
            if (present[first] && present[fourth]) {
                bool expected = false;
                if (found.compare_exchange_strong(expected, true)) {
                    witness = {first, middle_left, middle_right, fourth};
                }
                break;
            }
        }
    }
    return {found.load(), witness};
}

void verify_left_schedule(const vector<int>& state, int separation) {
    const vector<int> generated = raw(state, separation);
    unordered_set<int> working(generated.begin(), generated.end());
    vector<int> sponsors = {0};
    sponsors.insert(sponsors.end(), state.begin(), state.end());
    for (int sponsor : sponsors) {
        for (int layer = 0; layer < 3; ++layer) {
            if (!working.count(sponsor + layer * separation)) {
                throw runtime_error("infeasible left-sponsor schedule");
            }
        }
        working.erase(sponsor);
    }
}
} // namespace

int main() {
    const vector<int> s8 = build_s8();
    if (s8.size() != 29523 || s8.front() != L8 || s8.back() != 14604604) {
        throw runtime_error("unexpected S8 geometry");
    }

    const vector<int> at_twice_scale = raw(s8, 2 * L8);
    const auto invalid_witness = first_four_ap(at_twice_scale, L9);
    if (!invalid_witness.first) throw runtime_error("R=2L8 unexpectedly valid");

    int first_valid = 0;
    for (int separation = 2 * L8; separation <= R8; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        const vector<int> candidate = raw(s8, separation);
        if (candidate.size() != 3 * (s8.size() + 1)) continue;
        if (candidate.back() >= L9) continue;
        if (!first_four_ap(candidate, L9).first) {
            first_valid = separation;
            break;
        }
    }
    if (first_valid != R8) throw runtime_error("first exact recovery mismatch");

    const vector<int> g9 = raw(s8, R8);
    if (v2(R8) != 0 || g9.size() != 88572 || g9.front() != 0 ||
        g9.back() != 48159038 || fnv_hash(g9) != G9_FNV) {
        throw runtime_error("G9 mismatch");
    }
    if (first_four_ap(g9, L9).first) throw runtime_error("G9 contains a 4-AP");

    verify_left_schedule(s8, R8);
    vector<int> backbone;
    for (int value : g9) {
        if (L8 <= value && value < 2 * L8) backbone.push_back(value);
    }
    if (backbone != s8) throw runtime_error("factor-eight backbone is not exact");

    const vector<int> s9 = translate(g9, L9);
    if (s9.size() != 88572 || s9.front() != L9 || s9.back() != 115267902 ||
        fnv_hash(s9) != S9_FNV) {
        throw runtime_error("S9 mismatch");
    }

    cout << "verified: R=2L8 is invalid and R8=16777217 is first valid exact recovery\n";
    cout << "R_2L_witness=" << invalid_witness.second[0] << ","
         << invalid_witness.second[1] << "," << invalid_witness.second[2]
         << "," << invalid_witness.second[3] << "\n";
    cout << "scale_factors=4,8,4,4,8,4,8,8\n";
    cout << "state_size_S9=88572\n";
    cout << "weighted_density_S9=22143/32768\n";
    cout << "weighted_density_growth_S9_over_S8=7381/9841\n";
    cout << "G9_fnv64=a323906d13700252\n";
    cout << "S9_fnv64=5005dc89644a7b80\n";
    return 0;
}
