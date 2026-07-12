#include <algorithm>
#include <climits>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <unordered_set>
#include <vector>
#include <omp.h>

using namespace std;

namespace {
constexpr int L7 = 1048576;
constexpr int MAX_R = 1086317;

int v2(int value) {
    if (value <= 0) throw invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(value));
}

vector<int> unique_sorted(vector<int> values) {
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    return values;
}

vector<int> three_translate_raw(const vector<int>& state, int separation) {
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
        state = translate(
            three_translate_raw(state, separations[index]),
            scales[index + 1]
        );
    }

    state = translate(three_translate_raw(state, 93476), 262144);
    state = translate(three_translate_raw(state, 230164), L7);
    return state;
}
} // namespace

int main() {
    const double start_time = omp_get_wtime();
    const vector<int> state = build_s7();
    if (state.size() != 9840 || state.front() != L7 || state.back() != 2021668) {
        throw runtime_error("unexpected S7 geometry");
    }

    vector<int> base = {0};
    base.insert(base.end(), state.begin(), state.end());
    unordered_set<int> base_set(base.begin(), base.end());

    // A separation is layer-disjoint iff neither R nor 2R is a positive
    // difference of two base points.
    vector<unsigned char> difference(2 * MAX_R + 1, 0);
    for (int i = 0; i < static_cast<int>(base.size()); ++i) {
        for (int j = i + 1; j < static_cast<int>(base.size()); ++j) {
            const int delta = base[j] - base[i];
            if (delta > 2 * MAX_R) break;
            difference[delta] = 1;
        }
    }

    vector<int> candidates;
    vector<unsigned char> candidate_mask(MAX_R + 1, 0);
    int sponsor_candidate_count = 0;
    for (int separation = 1; separation <= MAX_R; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        ++sponsor_candidate_count;
        if (!difference[separation] && !difference[2 * separation]) {
            candidates.push_back(separation);
            candidate_mask[separation] = 1;
        }
    }

    if (sponsor_candidate_count != 724212 || candidates.size() != 359419) {
        throw runtime_error("factor-four candidate-domain mismatch");
    }

    vector<unsigned char> covered(MAX_R + 1, 0);
    vector<unsigned char> witness_class(MAX_R + 1, 0);

    // Class 1: one base second difference vanishes.  A positive base 3-AP
    // has a missing left or right completion z.  If b is another base point
    // with |z-b| = kR for k in {1,2,3}, one of the available layer patterns
    // with second-difference coefficient +/-k supplies a nontrivial 4-AP.
    set<int> right_completions;
    set<int> left_completions;
    for (int first_middle : base) {
        for (int second_middle : base) {
            if (second_middle <= first_middle) continue;
            if (base_set.count(2 * first_middle - second_middle)) {
                right_completions.insert(2 * second_middle - first_middle);
            }
            if (base_set.count(2 * second_middle - first_middle)) {
                left_completions.insert(2 * first_middle - second_middle);
            }
        }
    }

    auto add_completion_witnesses = [&](const set<int>& completions) {
        for (int completion : completions) {
            const auto lower = lower_bound(
                base.begin(), base.end(), completion - 3LL * MAX_R
            );
            const auto upper = upper_bound(
                base.begin(), base.end(), completion + 3LL * MAX_R
            );
            for (auto iterator = lower; iterator != upper; ++iterator) {
                const long long delta = llabs(static_cast<long long>(completion) - *iterator);
                if (delta == 0) continue;

                int separation = static_cast<int>(delta);
                if (separation <= MAX_R) covered[separation] = 1;

                if ((delta & 1LL) == 0) {
                    separation = static_cast<int>(delta / 2);
                    if (separation <= MAX_R) covered[separation] = 1;
                }
                if (delta % 3 == 0) {
                    separation = static_cast<int>(delta / 3);
                    if (separation <= MAX_R) covered[separation] = 1;
                }
            }
        }
    };

    add_completion_witnesses(right_completions);
    add_completion_witnesses(left_completions);

    vector<int> unresolved;
    int completion_witness_count = 0;
    for (int separation : candidates) {
        if (covered[separation]) {
            witness_class[separation] = 1;
            ++completion_witness_count;
        } else {
            unresolved.push_back(separation);
        }
    }
    if (completion_witness_count != 352979 || unresolved.size() != 6440) {
        throw runtime_error("completion-witness count mismatch");
    }

    // Difference statistics shared by the final two witness classes.
    const int maximum_base = base.back();
    vector<int> count(maximum_base + 1, 0);
    vector<int> minimum_start(maximum_base + 1, INT_MAX);
    vector<int> maximum_start(maximum_base + 1, INT_MIN);

    for (int i = 0; i < static_cast<int>(base.size()); ++i) {
        for (int j = i + 1; j < static_cast<int>(base.size()); ++j) {
            const int delta = base[j] - base[i];
            ++count[delta];
            minimum_start[delta] = min(minimum_start[delta], base[i]);
            maximum_start[delta] = max(maximum_start[delta], base[i]);
        }
    }

    // Class 2, layer pattern 1001.  A pair (y,y+3d) and a pair
    // (x,x+d) yield the actual 4-AP
    //
    //     y+R, x, x+d, y+3d+R
    //
    // when R = x-y-d.
    int lower_q = unresolved.front();
    int upper_q = unresolved.back();
    vector<unsigned char> needed_difference(maximum_base + 1, 0);
    vector<int> selected_differences;

    for (int delta = 1; 3LL * delta <= maximum_base; ++delta) {
        if (!count[delta] || !count[3 * delta]) continue;
        const long long minimum_q =
            static_cast<long long>(minimum_start[delta]) -
            maximum_start[3 * delta] - delta;
        const long long maximum_q =
            static_cast<long long>(maximum_start[delta]) -
            minimum_start[3 * delta] - delta;
        if (maximum_q >= lower_q && minimum_q <= upper_q) {
            selected_differences.push_back(delta);
            needed_difference[delta] = 1;
            needed_difference[3 * delta] = 1;
        }
    }

    vector<vector<int>> starts(maximum_base + 1);
    for (int delta = 1; delta <= maximum_base; ++delta) {
        if (needed_difference[delta]) starts[delta].reserve(count[delta]);
    }
    for (int i = 0; i < static_cast<int>(base.size()); ++i) {
        for (int j = i + 1; j < static_cast<int>(base.size()); ++j) {
            const int delta = base[j] - base[i];
            if (needed_difference[delta]) starts[delta].push_back(base[i]);
        }
    }

    for (int delta : selected_differences) {
        for (int inner_start : starts[delta]) {
            for (int outer_start : starts[3 * delta]) {
                const long long separation =
                    static_cast<long long>(inner_start) - outer_start - delta;
                if (
                    separation >= 1 && separation <= MAX_R &&
                    candidate_mask[separation] && !covered[separation]
                ) {
                    covered[separation] = 1;
                    witness_class[separation] = 2;
                }
            }
        }
    }

    unresolved.clear();
    int layer_1001_witness_count = 0;
    for (int separation : candidates) {
        if (witness_class[separation] == 2) ++layer_1001_witness_count;
        if (!covered[separation]) unresolved.push_back(separation);
    }
    if (layer_1001_witness_count != 215 || unresolved.size() != 6225) {
        throw runtime_error("layer-pattern 1001 count mismatch");
    }

    // Class 3, layer pattern 0011.  Equal-difference pairs
    // (x,x+d) and (y,y+d) yield the actual 4-AP
    //
    //     x, x+d, y+R, y+d+R
    //
    // when R = x+2d-y.
    lower_q = unresolved.front();
    upper_q = unresolved.back();
    vector<unsigned char> selected(maximum_base + 1, 0);
    vector<int> equal_difference_groups;

    for (int delta = 1; delta <= maximum_base; ++delta) {
        if (!count[delta]) continue;
        const int span = maximum_start[delta] - minimum_start[delta];
        if (
            2LL * delta + span >= lower_q &&
            2LL * delta - span <= upper_q
        ) {
            selected[delta] = 1;
            equal_difference_groups.push_back(delta);
        }
    }

    vector<vector<int>> equal_starts(maximum_base + 1);
    for (int delta : equal_difference_groups) {
        equal_starts[delta].reserve(count[delta]);
    }
    for (int i = 0; i < static_cast<int>(base.size()); ++i) {
        for (int j = i + 1; j < static_cast<int>(base.size()); ++j) {
            const int delta = base[j] - base[i];
            if (selected[delta]) equal_starts[delta].push_back(base[i]);
        }
    }

    vector<unsigned char> final_mark(MAX_R + 1, 0);
#pragma omp parallel for schedule(dynamic,64)
    for (int group = 0; group < static_cast<int>(equal_difference_groups.size()); ++group) {
        const int delta = equal_difference_groups[group];
        const vector<int>& values = equal_starts[delta];
        for (int first_start : values) {
            const long long minimum_second =
                static_cast<long long>(first_start) + 2LL * delta - upper_q;
            const long long maximum_second =
                static_cast<long long>(first_start) + 2LL * delta - lower_q;
            const auto lower = lower_bound(values.begin(), values.end(), minimum_second);
            const auto upper = upper_bound(values.begin(), values.end(), maximum_second);
            for (auto iterator = lower; iterator != upper; ++iterator) {
                const long long separation =
                    static_cast<long long>(first_start) + 2LL * delta - *iterator;
                if (
                    separation >= 1 && separation <= MAX_R &&
                    candidate_mask[separation] && !covered[separation]
                ) {
                    final_mark[separation] = 1;
                }
            }
        }
    }

    int layer_0011_witness_count = 0;
    int uncovered_count = 0;
    for (int separation : candidates) {
        if (final_mark[separation]) {
            covered[separation] = 1;
            witness_class[separation] = 3;
            ++layer_0011_witness_count;
        }
        if (!covered[separation]) ++uncovered_count;
    }

    if (layer_0011_witness_count != 6225 || uncovered_count != 0) {
        throw runtime_error("layer-pattern 0011 coverage mismatch");
    }

    cout << "verified: S7 has no factor-four continuation\n";
    cout << "maximum_separation=1086317\n";
    cout << "sponsor_candidate_count=724212\n";
    cout << "disjoint_candidate_count=359419\n";
    cout << "completion_witness_count=352979\n";
    cout << "layer_1001_witness_count=215\n";
    cout << "layer_0011_witness_count=6225\n";
    cout << "valid_count=0\n";
    cout << "seconds=" << (omp_get_wtime() - start_time) << "\n";
    return 0;
}
