#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace {

constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;
constexpr uint64_t EXPECTED_S7_FNV = 0xd1cfd1ae8b1faadaULL;

struct Witness {
    int p0 = 0;
    int p1 = 0;
    int p2 = 0;
    int p3 = 0;
    int missing_index = -1;
};

vector<int> unique_sorted(vector<int> values) {
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    return values;
}

vector<int> raw_three_translate(const vector<int>& state, int separation) {
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

vector<int> build_s7() {
    vector<int> base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28};
    const array<int, 7> scales = {64, 256, 2048, 8192, 32768, 262144, 1048576};
    const array<int, 6> separations = {61, 303, 1597, 8195, 93476, 230164};

    vector<int> state;
    for (int value : base) state.push_back(scales[0] + value);
    state = unique_sorted(move(state));
    for (size_t index = 0; index < separations.size(); ++index) {
        state = raw_three_translate(state, separations[index]);
        for (int& value : state) value += scales[index + 1];
        state = unique_sorted(move(state));
    }
    return state;
}

uint64_t fnv_values(const vector<int>& values) {
    uint64_t hash = FNV_OFFSET;
    for (int value : values) {
        string token = to_string(value) + ",";
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }
    return hash;
}

}  // namespace

int main() {
    vector<int> s7 = build_s7();
    if (s7.size() != 9840 || s7.front() != 1048576 || s7.back() != 2021668) {
        throw runtime_error("certified S7 reconstruction mismatch");
    }
    if (fnv_values(s7) != EXPECTED_S7_FNV) {
        throw runtime_error("certified S7 FNV mismatch");
    }

    const int lower = 1048576;
    const int upper = 2097151;
    vector<uint8_t> in_s7((size_t)(upper - lower + 1));
    vector<uint8_t> witnessed((size_t)(upper - lower + 1));
    vector<Witness> witnesses((size_t)(upper - lower + 1));
    for (int value : s7) in_s7[(size_t)(value - lower)] = 1;

    auto record = [&](long long hole, int p0, int p1, int p2, int p3,
                      int missing_index) {
        if (hole < lower || hole > upper) return;
        size_t offset = (size_t)(hole - lower);
        if (in_s7[offset] || witnessed[offset]) return;
        array<int, 4> points = {p0, p1, p2, p3};
        if (missing_index < 0 || missing_index > 3 ||
            points[(size_t)missing_index] != hole) {
            throw runtime_error("malformed four-AP witness");
        }
        int step = points[1] - points[0];
        if (step <= 0 || points[2] - points[1] != step ||
            points[3] - points[2] != step) {
            throw runtime_error("recorded witness is not a four-AP");
        }
        for (int index = 0; index < 4; ++index) {
            if (index == missing_index) continue;
            int value = points[(size_t)index];
            if (value < lower || value > upper ||
                !in_s7[(size_t)(value - lower)]) {
                throw runtime_error("recorded witness uses non-S7 support");
            }
        }
        witnessed[offset] = 1;
        witnesses[offset] = {p0, p1, p2, p3, missing_index};
    };

    long long pair_checks = 0;
    for (int left_index = 0; left_index < (int)s7.size(); ++left_index) {
        int left = s7[(size_t)left_index];
        for (int right_index = left_index + 1;
             right_index < (int)s7.size(); ++right_index) {
            int right = s7[(size_t)right_index];
            int step = right - left;
            ++pair_checks;

            long long next = (long long)right + step;
            if (next <= upper && in_s7[(size_t)(next - lower)]) {
                record((long long)right + 2LL * step,
                       left, right, (int)next, right + 2 * step, 3);
                record((long long)left - step,
                       left - step, left, right, (int)next, 0);
            }

            long long far_right = (long long)right + 2LL * step;
            if (far_right <= upper && in_s7[(size_t)(far_right - lower)]) {
                record((long long)right + step,
                       left, right, right + step, (int)far_right, 2);
            }

            long long far_left = (long long)left - 2LL * step;
            if (far_left >= lower && in_s7[(size_t)(far_left - lower)]) {
                record((long long)left - step,
                       (int)far_left, left - step, left, right, 1);
            }
        }
    }

    long long hole_count = 0;
    cout << "completion\tp0\tp1\tp2\tp3\tmissing_index\n";
    for (int completion = lower; completion <= upper; ++completion) {
        size_t offset = (size_t)(completion - lower);
        if (!witnessed[offset]) continue;
        const Witness& witness = witnesses[offset];
        cout << completion << '\t'
             << witness.p0 << '\t' << witness.p1 << '\t'
             << witness.p2 << '\t' << witness.p3 << '\t'
             << witness.missing_index << '\n';
        ++hole_count;
    }

    cerr << "s7_points=" << s7.size() << '\n';
    cerr << "pair_checks=" << pair_checks << '\n';
    cerr << "certified_shell_holes=" << hole_count << '\n';
    cerr << "S7_shell_admissible_absent="
         << (upper - lower + 1 - (long long)s7.size() - hole_count) << '\n';
    return 0;
}
