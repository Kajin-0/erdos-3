#include <algorithm>
#include <array>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>

using namespace std;

namespace {
constexpr int L8 = 8388608;
constexpr int MAX_R2 = 1086305;
constexpr int MAX_R4 = 9474913;
constexpr uint64_t S8_FNV = 0x023db79dd7cbf62bULL;
constexpr uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr uint64_t FNV_PRIME = 1099511628211ULL;

int v2(int x) {
    if (x <= 0) throw invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(x));
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

inline void set_bit(vector<uint64_t>& bits, long long index) {
    bits[index >> 6] |= 1ULL << (index & 63);
}

inline bool get_bit(const vector<uint64_t>& bits, long long index) {
    return (bits[index >> 6] >> (index & 63)) & 1ULL;
}

vector<uint64_t> positive_difference_support(
    const vector<int>& base,
    int maximum_delta,
    int threads
) {
    const size_t words = (maximum_delta + 64LL) / 64;
    vector<vector<uint64_t>> local(threads, vector<uint64_t>(words));
#pragma omp parallel num_threads(threads)
    {
        const int thread = omp_get_thread_num();
        auto& bits = local[thread];
#pragma omp for schedule(dynamic,4)
        for (int first = 0; first < static_cast<int>(base.size()); ++first) {
            for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
                const int delta = base[second] - base[first];
                if (delta > maximum_delta) break;
                set_bit(bits, delta);
            }
        }
    }
    vector<uint64_t> result(words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < words; ++word) result[word] |= bits[word];
    }
    return result;
}

struct Domain {
    vector<int> candidates;
    long long sponsor_count = 0;
};

Domain candidate_domain(const vector<uint64_t>& differences, int maximum_r) {
    Domain result;
    for (int separation = 1; separation <= maximum_r; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        ++result.sponsor_count;
        if (!get_bit(differences, separation) &&
            !get_bit(differences, 2LL * separation)) {
            result.candidates.push_back(separation);
        }
    }
    return result;
}

vector<int> completion_coordinates(const vector<int>& base, int threads) {
    const int maximum = base.back();
    const int offset = maximum;
    const int range = 3 * maximum + 1;
    vector<unsigned char> present(maximum + 1);
    for (int value : base) present[value] = 1;
    const size_t words = (range + 63LL) / 64;
    vector<vector<uint64_t>> local(threads, vector<uint64_t>(words));
#pragma omp parallel num_threads(threads)
    {
        const int thread = omp_get_thread_num();
        auto& bits = local[thread];
#pragma omp for schedule(dynamic,4)
        for (int first = 0; first < static_cast<int>(base.size()); ++first) {
            const int a = base[first];
            for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
                const int b = base[second];
                const int left = 2 * a - b;
                const int right = 2 * b - a;
                if (left >= 0 && present[left]) set_bit(bits, static_cast<long long>(right) + offset);
                if (right <= maximum && present[right]) set_bit(bits, static_cast<long long>(left) + offset);
            }
        }
    }
    vector<uint64_t> all(words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < words; ++word) all[word] |= bits[word];
    }
    vector<int> completions;
    for (int index = 0; index < range; ++index) {
        if (get_bit(all, index)) completions.push_back(index - offset);
    }
    return completions;
}

vector<uint64_t> exact_completion_difference_support(
    const vector<int>& base,
    const vector<int>& completions,
    int threads
) {
    const int maximum = base.back();
    const int maximum_completion = completions.back();
    const size_t completion_words = (maximum_completion + 64LL) / 64;
    const size_t output_words = (static_cast<long long>(maximum) + maximum_completion + 64) / 64;
    vector<uint64_t> completion_bits(completion_words);
    for (int completion : completions) set_bit(completion_bits, completion);
    vector<vector<uint64_t>> local(threads, vector<uint64_t>(output_words));
#pragma omp parallel num_threads(threads)
    {
        const int thread = omp_get_thread_num();
        auto& output = local[thread];
#pragma omp for schedule(static)
        for (int base_index = 0; base_index < static_cast<int>(base.size()); ++base_index) {
            const long long shift = static_cast<long long>(maximum) - base[base_index];
            const size_t word_shift = shift >> 6;
            const int bit_shift = shift & 63;
            if (bit_shift == 0) {
                for (size_t word = 0; word < completion_words; ++word) {
                    output[word_shift + word] |= completion_bits[word];
                }
            } else {
                const int reverse_shift = 64 - bit_shift;
                for (size_t word = 0; word < completion_words; ++word) {
                    const uint64_t value = completion_bits[word];
                    output[word_shift + word] |= value << bit_shift;
                    if (word_shift + word + 1 < output_words) {
                        output[word_shift + word + 1] |= value >> reverse_shift;
                    }
                }
            }
        }
    }
    vector<uint64_t> result(output_words);
    for (const auto& bits : local) {
        for (size_t word = 0; word < output_words; ++word) result[word] |= bits[word];
    }
    return result;
}

bool completion_hit(const vector<uint64_t>& support, int maximum, int separation) {
    const long long limit = static_cast<long long>(support.size()) * 64;
    for (int multiplier = 1; multiplier <= 3; ++multiplier) {
        const long long difference = 1LL * multiplier * separation;
        if (maximum + difference < limit && get_bit(support, maximum + difference)) return true;
        if (maximum - difference >= 0 && get_bit(support, maximum - difference)) return true;
    }
    return false;
}

struct DifferenceStats {
    vector<int> count;
    vector<int> minimum_start;
    vector<int> maximum_start;
};

DifferenceStats difference_stats(const vector<int>& base) {
    const int maximum = base.back();
    DifferenceStats result{
        vector<int>(maximum + 1),
        vector<int>(maximum + 1, INT_MAX),
        vector<int>(maximum + 1, INT_MIN)
    };
    for (int first = 0; first < static_cast<int>(base.size()); ++first) {
        for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
            const int difference = base[second] - base[first];
            ++result.count[difference];
            result.minimum_start[difference] = min(result.minimum_start[difference], base[first]);
            result.maximum_start[difference] = max(result.maximum_start[difference], base[first]);
        }
    }
    return result;
}

vector<int> apply_pattern_1001(
    const vector<int>& base,
    const DifferenceStats& stats,
    const vector<int>& targets,
    int& covered_count
) {
    const int maximum = base.back();
    const int maximum_r = targets.back();
    vector<unsigned char> target(maximum_r + 1);
    vector<unsigned char> covered(maximum_r + 1);
    vector<unsigned char> needed(maximum + 1);
    for (int separation : targets) target[separation] = 1;
    const int lower_target = targets.front();
    const int upper_target = targets.back();
    vector<int> selected_differences;
    for (int difference = 1; 3LL * difference <= maximum; ++difference) {
        if (!stats.count[difference] || !stats.count[3 * difference]) continue;
        const long long minimum_separation =
            static_cast<long long>(stats.minimum_start[difference]) -
            stats.maximum_start[3 * difference] - difference;
        const long long maximum_separation =
            static_cast<long long>(stats.maximum_start[difference]) -
            stats.minimum_start[3 * difference] - difference;
        if (maximum_separation >= lower_target && minimum_separation <= upper_target) {
            selected_differences.push_back(difference);
            needed[difference] = 1;
            needed[3 * difference] = 1;
        }
    }
    if (selected_differences.size() != 4801) {
        throw runtime_error("1001 selected-difference mismatch");
    }
    vector<int> index(maximum + 1, -1);
    vector<int> needed_differences;
    long long pair_total = 0;
    for (int difference = 1; difference <= maximum; ++difference) {
        if (needed[difference]) {
            index[difference] = needed_differences.size();
            needed_differences.push_back(difference);
            pair_total += stats.count[difference];
        }
    }
    if (needed_differences.size() != 9602 || pair_total != 725809) {
        throw runtime_error("1001 pair-domain mismatch");
    }
    vector<vector<int>> starts(needed_differences.size());
    for (int entry = 0; entry < static_cast<int>(needed_differences.size()); ++entry) {
        starts[entry].reserve(stats.count[needed_differences[entry]]);
    }
    for (int first = 0; first < static_cast<int>(base.size()); ++first) {
        for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
            const int difference = base[second] - base[first];
            const int entry = index[difference];
            if (entry >= 0) starts[entry].push_back(base[first]);
        }
    }
    long long combinations = 0;
    for (int difference : selected_differences) {
        const auto& inner = starts[index[difference]];
        const auto& outer = starts[index[3 * difference]];
        for (int inner_start : inner) {
            const long long minimum_outer =
                static_cast<long long>(inner_start) - difference - upper_target;
            const long long maximum_outer =
                static_cast<long long>(inner_start) - difference - lower_target;
            const auto lower = lower_bound(outer.begin(), outer.end(), minimum_outer);
            const auto upper = upper_bound(outer.begin(), outer.end(), maximum_outer);
            for (auto iterator = lower; iterator != upper; ++iterator) {
                ++combinations;
                const long long separation =
                    static_cast<long long>(inner_start) - *iterator - difference;
                if (separation >= 1 && separation <= maximum_r && target[separation]) {
                    covered[separation] = 1;
                }
            }
        }
    }
    if (combinations != 509532) throw runtime_error("1001 combination mismatch");
    vector<int> remaining;
    covered_count = 0;
    for (int separation : targets) {
        if (covered[separation]) ++covered_count;
        else remaining.push_back(separation);
    }
    if (covered_count != 73 || remaining.size() != 748043) {
        throw runtime_error("1001 coverage mismatch");
    }
    return remaining;
}

struct PhaseResult {
    vector<int> remaining;
    int processed_groups;
    long long operations;
};

PhaseResult run_pattern_0011_phase(
    const vector<int>& base,
    const DifferenceStats& stats,
    const vector<int>& targets,
    long long budget,
    int skipped_groups
) {
    const int maximum = base.back();
    const int lower_target = targets.front();
    const int upper_target = targets.back();
    const int maximum_r = targets.back();
    vector<unsigned char> target(maximum_r + 1);
    vector<unsigned char> covered(maximum_r + 1);
    for (int separation : targets) target[separation] = 1;

    vector<int> group_index(maximum + 1, -1);
    vector<int> groups;
    long long total_starts = 0;
    for (int difference = 1; difference <= maximum; ++difference) {
        if (!stats.count[difference]) continue;
        const int span =
            stats.maximum_start[difference] - stats.minimum_start[difference];
        if (2LL * difference + span >= lower_target &&
            2LL * difference - span <= upper_target) {
            group_index[difference] = groups.size();
            groups.push_back(difference);
            total_starts += stats.count[difference];
        }
    }

    vector<uint64_t> offsets(groups.size() + 1);
    for (size_t group = 0; group < groups.size(); ++group) {
        offsets[group + 1] = offsets[group] + stats.count[groups[group]];
    }
    vector<uint64_t> cursors = offsets;
    int* starts = new int[total_starts];
    for (int first = 0; first < static_cast<int>(base.size()); ++first) {
        for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
            const int difference = base[second] - base[first];
            const int group = group_index[difference];
            if (group >= 0) starts[cursors[group]++] = base[first];
        }
    }

    vector<int> order(groups.size());
    for (int group = 0; group < static_cast<int>(groups.size()); ++group) order[group] = group;
    sort(order.begin(), order.end(), [&](int first_group, int second_group) {
        const long long first_difference = groups[first_group];
        const long long second_difference = groups[second_group];
        const bool first_inside =
            2 * first_difference >= lower_target && 2 * first_difference <= upper_target;
        const bool second_inside =
            2 * second_difference >= lower_target && 2 * second_difference <= upper_target;
        if (first_inside != second_inside) return first_inside > second_inside;
        const long long first_distance =
            2 * first_difference < lower_target ? lower_target - 2 * first_difference :
            (2 * first_difference > upper_target ? 2 * first_difference - upper_target : 0);
        const long long second_distance =
            2 * second_difference < lower_target ? lower_target - 2 * second_difference :
            (2 * second_difference > upper_target ? 2 * second_difference - upper_target : 0);
        if (first_distance != second_distance) return first_distance < second_distance;
        return stats.count[groups[first_group]] > stats.count[groups[second_group]];
    });

    long long operations = 0;
    int processed_groups = 0;
    for (int ordered = skipped_groups; ordered < static_cast<int>(order.size()); ++ordered) {
        const int group = order[ordered];
        const int difference = groups[group];
        const int count = offsets[group + 1] - offsets[group];
        int* values = starts + offsets[group];
        for (int first = 0; first < count; ++first) {
            for (int second = 0; second <= first; ++second) {
                const int delta = values[first] - values[second];
                const int separation_plus = 2 * difference + delta;
                const int separation_minus = 2 * difference - delta;
                if (separation_plus >= 1 && separation_plus <= maximum_r &&
                    target[separation_plus]) {
                    covered[separation_plus] = 1;
                }
                if (delta && separation_minus >= 1 && separation_minus <= maximum_r &&
                    target[separation_minus]) {
                    covered[separation_minus] = 1;
                }
                if (++operations >= budget) goto complete;
            }
        }
        ++processed_groups;
    }
complete:
    vector<int> remaining;
    for (int separation : targets) {
        if (!covered[separation]) remaining.push_back(separation);
    }
    delete[] starts;
    return {move(remaining), processed_groups, operations};
}

void check_phase(
    const PhaseResult& phase,
    int expected_processed,
    size_t expected_remaining,
    uint64_t expected_hash
) {
    if (phase.processed_groups != expected_processed ||
        phase.remaining.size() != expected_remaining ||
        fnv_values(phase.remaining) != expected_hash) {
        throw runtime_error("0011 phase mismatch");
    }
}

void verify_exception(
    const vector<int>& base,
    int separation,
    const array<int,4>& progression,
    const array<int,4>& base_points
) {
    unordered_set<int> base_set(base.begin(), base.end());
    const int difference = progression[1] - progression[0];
    if (difference <= 0 || progression[2] - progression[1] != difference ||
        progression[3] - progression[2] != difference) {
        throw runtime_error("exception is not a four-term progression");
    }
    for (int index = 0; index < 4; ++index) {
        const int layer = index < 2 ? 0 : 1;
        if (progression[index] != base_points[index] + layer * separation ||
            !base_set.count(base_points[index])) {
            throw runtime_error("exception layer mismatch");
        }
    }
    if (base_points[1] - base_points[0] != base_points[3] - base_points[2]) {
        throw runtime_error("exception is not an 0011 witness");
    }
}

struct CoreResult {
    vector<int> base;
    DifferenceStats stats;
    vector<int> targets;
};

CoreResult prepare_core(int threads) {
    vector<int> s8 = build_s8();
    if (s8.size() != 29523 || s8.front() != L8 || s8.back() != 14604604 ||
        fnv_values(s8) != S8_FNV) {
        throw runtime_error("S8 mismatch");
    }
    vector<int> base = {0};
    base.insert(base.end(), s8.begin(), s8.end());

    vector<uint64_t> differences = positive_difference_support(base, 2 * MAX_R4, threads);
    Domain factor_two = candidate_domain(differences, MAX_R2);
    Domain factor_four = candidate_domain(differences, MAX_R4);
    if (factor_two.sponsor_count != 724204 || factor_two.candidates.size() != 172448) {
        throw runtime_error("factor-two domain mismatch");
    }
    if (factor_four.sponsor_count != 6316609 || factor_four.candidates.size() != 4190292) {
        throw runtime_error("factor-four domain mismatch");
    }
    differences.clear();
    differences.shrink_to_fit();

    vector<int> completions = completion_coordinates(base, threads);
    if (completions.size() != 2772873 || completions.front() != 6291444 ||
        completions.back() != 17038008) {
        throw runtime_error("completion set mismatch");
    }
    vector<uint64_t> completion_support =
        exact_completion_difference_support(base, completions, threads);
    completions.clear();
    completions.shrink_to_fit();

    const int maximum = base.back();
    int factor_two_covered = 0;
    int factor_four_covered = 0;
    vector<int> unresolved_factor_four;
    for (int separation : factor_two.candidates) {
        if (completion_hit(completion_support, maximum, separation)) ++factor_two_covered;
    }
    for (int separation : factor_four.candidates) {
        if (completion_hit(completion_support, maximum, separation)) ++factor_four_covered;
        else unresolved_factor_four.push_back(separation);
    }
    if (factor_two_covered != 172448 || factor_four_covered != 3442176 ||
        unresolved_factor_four.size() != 748116) {
        throw runtime_error("completion coverage mismatch");
    }
    completion_support.clear();
    completion_support.shrink_to_fit();
    factor_two.candidates.clear();
    factor_two.candidates.shrink_to_fit();
    factor_four.candidates.clear();
    factor_four.candidates.shrink_to_fit();

    DifferenceStats stats = difference_stats(base);
    int pattern_1001_covered = 0;
    vector<int> targets =
        apply_pattern_1001(base, stats, unresolved_factor_four, pattern_1001_covered);
    if (fnv_values(targets) != 0xb8ddbb02d22c7ca4ULL) {
        throw runtime_error("post-1001 hash mismatch");
    }

    cout << "factor2_sponsor_candidates=724204\n";
    cout << "factor2_disjoint_candidates=172448\n";
    cout << "factor2_completion_witnesses=172448\n";
    cout << "factor4_sponsor_candidates=6316609\n";
    cout << "factor4_disjoint_candidates=4190292\n";
    cout << "factor4_completion_witnesses=3442176\n";
    cout << "factor4_pattern1001_witnesses=73\n";
    cout << "post1001_remaining=748043\n";
    return {move(base), move(stats), move(targets)};
}

vector<int> read_targets(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open target file: " + path);
    vector<int> values;
    int value;
    while (input >> value) values.push_back(value);
    if (values.empty()) throw runtime_error("empty target file");
    return values;
}

void write_targets(const string& path, const vector<int>& values) {
    if (path.empty()) return;
    ofstream output(path);
    if (!output) throw runtime_error("cannot write target file: " + path);
    for (int value : values) output << value << "\n";
}

void print_phase(const string& name, const PhaseResult& phase) {
    cout << name << "_processed_groups=" << phase.processed_groups << "\n";
    cout << name << "_operations=" << phase.operations << "\n";
    cout << name << "_remaining=" << phase.remaining.size() << "\n";
}
} // namespace

int main(int argc, char** argv) {
    string mode = "core";
    string target_file;
    string write_remaining;
    for (int index = 1; index < argc; ++index) {
        const string argument = argv[index];
        if (argument == "--mode" && index + 1 < argc) mode = argv[++index];
        else if (argument == "--target-file" && index + 1 < argc) {
            target_file = argv[++index];
        } else if (argument == "--write-remaining" && index + 1 < argc) {
            write_remaining = argv[++index];
        } else {
            throw invalid_argument(
                "usage: --mode core|phase1|phase2|phase3|phase4|phase5|exceptions "
                "[--target-file PATH] [--write-remaining PATH]"
            );
        }
    }

    const int threads = min(16, max(1, omp_get_max_threads()));
    if (mode == "core") {
        CoreResult core = prepare_core(threads);
        write_targets(write_remaining, core.targets);
        cout << "verified: exact S8 cheap-extension core\n";
        return 0;
    }

    vector<int> s8 = build_s8();
    vector<int> base = {0};
    base.insert(base.end(), s8.begin(), s8.end());
    DifferenceStats stats = difference_stats(base);

    if (mode == "phase1") {
        if (target_file.empty()) throw invalid_argument("phase1 requires --target-file");
        vector<int> targets = read_targets(target_file);
        if (targets.size() != 748043 || fnv_values(targets) != 0xb8ddbb02d22c7ca4ULL) {
            throw runtime_error("phase1 input mismatch");
        }
        PhaseResult phase = run_pattern_0011_phase(base, stats, targets, 2000000000LL, 0);
        check_phase(phase, 289, 27182, 0x7a7433cf08775279ULL);
        write_targets(write_remaining, phase.remaining);
        print_phase("phase1", phase);
        return 0;
    }
    if (mode == "phase2") {
        if (target_file.empty()) throw invalid_argument("phase2 requires --target-file");
        vector<int> targets = read_targets(target_file);
        if (targets.size() != 27182 || fnv_values(targets) != 0x7a7433cf08775279ULL) {
            throw runtime_error("phase2 input mismatch");
        }
        PhaseResult phase = run_pattern_0011_phase(base, stats, targets, 2000000000LL, 289);
        check_phase(phase, 900, 1266, 0x2cd2e22c6768791dULL);
        write_targets(write_remaining, phase.remaining);
        print_phase("phase2", phase);
        return 0;
    }
    if (mode == "phase3") {
        if (target_file.empty()) throw invalid_argument("phase3 requires --target-file");
        vector<int> targets = read_targets(target_file);
        if (targets.size() != 1266 || fnv_values(targets) != 0x2cd2e22c6768791dULL) {
            throw runtime_error("phase3 input mismatch");
        }
        PhaseResult phase = run_pattern_0011_phase(base, stats, targets, 2000000000LL, 1189);
        check_phase(phase, 1886, 45, 0xec113295ef522398ULL);
        write_targets(write_remaining, phase.remaining);
        print_phase("phase3", phase);
        return 0;
    }
    if (mode == "phase4") {
        if (target_file.empty()) throw invalid_argument("phase4 requires --target-file");
        vector<int> targets = read_targets(target_file);
        if (targets.size() != 45 || fnv_values(targets) != 0xec113295ef522398ULL) {
            throw runtime_error("phase4 input mismatch");
        }
        PhaseResult phase = run_pattern_0011_phase(base, stats, targets, 2000000000LL, 3075);
        check_phase(phase, 105273, 4, 0x1c87eedd7756042dULL);
        write_targets(write_remaining, phase.remaining);
        print_phase("phase4", phase);
        return 0;
    }
    if (mode == "phase5") {
        if (target_file.empty()) throw invalid_argument("phase5 requires --target-file");
        vector<int> targets = read_targets(target_file);
        if (targets.size() != 4 || fnv_values(targets) != 0x1c87eedd7756042dULL) {
            throw runtime_error("phase5 input mismatch");
        }
        PhaseResult phase = run_pattern_0011_phase(base, stats, targets, 5000000000LL, 108348);
        check_phase(phase, 128084, 3, 0x4ca400f49b2c73f1ULL);
        write_targets(write_remaining, phase.remaining);
        print_phase("phase5", phase);
        return 0;
    }
    if (mode == "exceptions") {
        verify_exception(
            base,
            5353028,
            {10161822,11951729,13741636,15531543},
            {10161822,11951729,8388608,10178515}
        );
        verify_exception(
            base,
            5353089,
            {8388608,12029053,15669498,19309943},
            {8388608,12029053,10316409,13956854}
        );
        verify_exception(
            base,
            5353229,
            {12035410,13893656,15751902,17610148},
            {12035410,13893656,10398673,12256919}
        );
        cout << "verified: three explicit terminal 0011 witnesses\n";
        cout << "N_8_2=0\n";
        cout << "N_8_4=0\n";
        return 0;
    }
    throw invalid_argument("unknown mode");
}
