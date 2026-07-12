#include <algorithm>
#include <array>
#include <atomic>
#include <cstdlib>
#include <iostream>
#include <mutex>
#include <stdexcept>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

namespace {
constexpr int L7 = 1048576;

int v2(int value) {
    if (value <= 0) throw std::invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(value));
}

std::vector<int> unique_sorted(std::vector<int> values) {
    std::sort(values.begin(), values.end());
    values.erase(std::unique(values.begin(), values.end()), values.end());
    return values;
}

std::vector<int> raw(const std::vector<int>& state, int separation) {
    std::vector<int> values;
    values.reserve(3 * (state.size() + 1));
    for (int layer = 0; layer < 3; ++layer) values.push_back(layer * separation);
    for (int value : state) {
        for (int layer = 0; layer < 3; ++layer) values.push_back(value + layer * separation);
    }
    return unique_sorted(std::move(values));
}

std::vector<int> shifted(const std::vector<int>& values, int offset) {
    std::vector<int> result;
    result.reserve(values.size());
    for (int value : values) result.push_back(offset + value);
    return result;
}

std::vector<int> build_s7() {
    const std::vector<int> H = {0,1,2,16,17,18,21,22,23,26,27,28};
    const std::array<int,5> scales = {64,256,2048,8192,32768};
    const std::array<int,4> separations = {61,303,1597,8195};
    std::vector<int> state;
    for (int value : H) state.push_back(scales[0] + value);
    state = unique_sorted(std::move(state));
    for (std::size_t index = 0; index < separations.size(); ++index) {
        state = shifted(raw(state, separations[index]), scales[index + 1]);
    }
    state = shifted(raw(state, 93476), 262144);
    state = shifted(raw(state, 230164), L7);
    return state;
}

class APChecker {
public:
    explicit APChecker(int maximum) : stamps_(maximum + 1, 0) {}

    bool has_four_ap(const std::vector<int>& values) {
        ++generation_;
        if (generation_ == 0) {
            std::fill(stamps_.begin(), stamps_.end(), 0);
            generation_ = 1;
        }
        for (int value : values) stamps_[value] = generation_;
        const int maximum = values.back();
        for (std::size_t i = 0; i < values.size(); ++i) {
            const int middle_left = values[i];
            const int upper = (maximum + middle_left) / 2;
            const auto stop = std::upper_bound(values.begin() + static_cast<long>(i) + 1, values.end(), upper);
            for (auto it = values.begin() + static_cast<long>(i) + 1; it != stop; ++it) {
                const int middle_right = *it;
                const int first = 2 * middle_left - middle_right;
                if (first < 0) continue;
                const int fourth = 2 * middle_right - middle_left;
                if (stamps_[first] == generation_ && stamps_[fourth] == generation_) return true;
            }
        }
        return false;
    }

private:
    std::vector<unsigned> stamps_;
    unsigned generation_ = 0;
};

long parse_long(const char* text, const char* name) {
    char* end = nullptr;
    const long value = std::strtol(text, &end, 10);
    if (!end || *end != '\0') throw std::invalid_argument(std::string("invalid ") + name);
    return value;
}

} // namespace

int main(int argc, char** argv) {
    long requested_start = 1;
    long requested_end = -1;
    for (int index = 1; index < argc; ++index) {
        const std::string argument = argv[index];
        if (argument == "--start" && index + 1 < argc) requested_start = parse_long(argv[++index], "start");
        else if (argument == "--end" && index + 1 < argc) requested_end = parse_long(argv[++index], "end");
        else throw std::invalid_argument("usage: search_depth7_factor4_extension [--start R] [--end R]");
    }

    const std::vector<int> s7 = build_s7();
    if (s7.size() != 9840 || s7.front() != L7 || s7.back() != 2021668) {
        throw std::runtime_error("unexpected S7 geometry");
    }

    const int next_scale = 4 * L7;
    const int maximum_r = (next_scale - 1 - s7.back()) / 2;
    if (maximum_r != 1086317) throw std::runtime_error("factor-four domain mismatch");
    const int start = static_cast<int>(std::max<long>(1, requested_start));
    const int end = static_cast<int>(requested_end < 0 ? maximum_r : std::min<long>(maximum_r, requested_end));
    if (end < start) throw std::invalid_argument("empty search range");

    std::vector<int> anchor = {0};
    anchor.insert(anchor.end(), s7.begin(), s7.end());
    const int difference_limit = 2 * maximum_r;
    std::vector<unsigned char> difference(difference_limit + 1, 0);
    for (std::size_t i = 0; i < anchor.size(); ++i) {
        for (std::size_t j = i + 1; j < anchor.size(); ++j) {
            const int delta = anchor[j] - anchor[i];
            if (delta > difference_limit) break;
            difference[delta] = 1;
        }
    }

    std::vector<int> candidates;
    std::vector<int> disjoint;
    for (int separation = start; separation <= end; ++separation) {
        if (v2(separation) % 2 != 0) continue;
        candidates.push_back(separation);
        if (!difference[separation] && !difference[2 * separation]) disjoint.push_back(separation);
    }

    std::atomic<int> tested{0};
    std::mutex valid_mutex;
    std::vector<int> valid;
#ifdef _OPENMP
#pragma omp parallel
#endif
    {
        APChecker checker(next_scale - 1);
#ifdef _OPENMP
#pragma omp for schedule(dynamic,1)
#endif
        for (std::size_t index = 0; index < disjoint.size(); ++index) {
            const int separation = disjoint[index];
            const std::vector<int> candidate_raw = raw(s7, separation);
            if (candidate_raw.size() != 3 * (s7.size() + 1)) continue;
            if (candidate_raw.back() >= next_scale) continue;
            const bool bad = checker.has_four_ap(candidate_raw);
            ++tested;
            if (!bad) {
                std::lock_guard<std::mutex> lock(valid_mutex);
                valid.push_back(separation);
            }
        }
    }

    std::sort(valid.begin(), valid.end());

    std::cout << "state_depth=7\n";
    std::cout << "state_size=9840\n";
    std::cout << "state_scale=1048576\n";
    std::cout << "factor=4\n";
    std::cout << "maximum_separation=1086317\n";
    std::cout << "start=" << start << "\n";
    std::cout << "end=" << end << "\n";
    std::cout << "sponsor_candidate_count=" << candidates.size() << "\n";
    std::cout << "disjoint_candidate_count=" << disjoint.size() << "\n";
    std::cout << "tested_disjoint_count=" << tested.load() << "\n";
    std::cout << "valid_count=" << valid.size() << "\n";
    for (int separation : valid) std::cout << "valid_separation=" << separation << "\n";
    return 0;
}
