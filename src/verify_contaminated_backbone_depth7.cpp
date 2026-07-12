#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

namespace {
constexpr int R5 = 93476;
constexpr int R6 = 230164;
constexpr int L5 = 32768;
constexpr int L6 = 262144;
constexpr int L7 = 1048576;
constexpr std::uint64_t FNV_OFFSET = 1469598103934665603ULL;
constexpr std::uint64_t FNV_PRIME = 1099511628211ULL;
constexpr std::uint64_t S5_FNV = 0x534fd1f8cef8c788ULL;
constexpr std::uint64_t G6_FNV = 0xbbf390929eafe9d0ULL;
constexpr std::uint64_t S6_FNV = 0x82f7a53866d615ecULL;
constexpr std::uint64_t G7_FNV = 0xa8e466af4e4bfcb2ULL;
constexpr std::uint64_t S7_FNV = 0xd1cfd1ae8b1faadaULL;

int v2(int value) {
    if (value <= 0) throw std::invalid_argument("v2 requires a positive integer");
    return __builtin_ctz(static_cast<unsigned>(value));
}

std::vector<int> unique_sorted(std::vector<int> values) {
    std::sort(values.begin(), values.end());
    values.erase(std::unique(values.begin(), values.end()), values.end());
    return values;
}

std::vector<int> three_translate_raw(const std::vector<int>& state, int separation) {
    std::vector<int> values;
    values.reserve(3 * (state.size() + 1));
    for (int layer = 0; layer < 3; ++layer) values.push_back(layer * separation);
    for (int value : state) {
        for (int layer = 0; layer < 3; ++layer) values.push_back(value + layer * separation);
    }
    return unique_sorted(std::move(values));
}

std::vector<int> translate(const std::vector<int>& values, int offset) {
    std::vector<int> result;
    result.reserve(values.size());
    for (int value : values) result.push_back(offset + value);
    return result;
}

std::vector<int> build_s5() {
    const std::vector<int> H = {0,1,2,16,17,18,21,22,23,26,27,28};
    const std::array<int,5> scales = {64,256,2048,8192,32768};
    const std::array<int,4> separations = {61,303,1597,8195};
    std::vector<int> state;
    for (int value : H) state.push_back(scales[0] + value);
    state = unique_sorted(std::move(state));
    for (std::size_t index = 0; index < separations.size(); ++index) {
        state = translate(three_translate_raw(state, separations[index]), scales[index + 1]);
    }
    return state;
}

std::uint64_t fnv_state(const std::vector<int>& values) {
    std::uint64_t hash = FNV_OFFSET;
    for (int value : values) {
        const std::string token = std::to_string(value) + ",";
        for (unsigned char byte : token) {
            hash ^= byte;
            hash *= FNV_PRIME;
        }
    }
    return hash;
}

class APChecker {
public:
    explicit APChecker(int maximum) : stamps_(maximum + 1, 0) {}

    bool has_four_ap(const std::vector<int>& values, std::array<int,4>* witness = nullptr) {
        ++generation_;
        if (generation_ == 0) {
            std::fill(stamps_.begin(), stamps_.end(), 0);
            generation_ = 1;
        }
        for (int value : values) stamps_.at(value) = generation_;
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
                if (stamps_[first] == generation_ && stamps_[fourth] == generation_) {
                    if (witness) *witness = {first, middle_left, middle_right, fourth};
                    return true;
                }
            }
        }
        return false;
    }

private:
    std::vector<unsigned> stamps_;
    unsigned generation_ = 0;
};

void verify_left_schedule(const std::vector<int>& state, int separation) {
    std::unordered_set<int> working;
    const std::vector<int> raw = three_translate_raw(state, separation);
    working.reserve(raw.size() * 2);
    for (int value : raw) working.insert(value);
    std::vector<int> sponsors = {0};
    sponsors.insert(sponsors.end(), state.begin(), state.end());
    for (int sponsor : sponsors) {
        for (int layer = 0; layer < 3; ++layer) {
            if (!working.count(sponsor + layer * separation)) {
                throw std::runtime_error("infeasible left-sponsor deletion schedule");
            }
        }
        working.erase(sponsor);
    }
}

std::vector<int> shell(const std::vector<int>& values, int scale) {
    std::vector<int> result;
    for (int value : values) if (scale <= value && value < 2 * scale) result.push_back(value);
    return result;
}

bool contains_all(const std::vector<int>& superset, const std::vector<int>& subset) {
    return std::includes(superset.begin(), superset.end(), subset.begin(), subset.end());
}

void verify_replication_step(
    const std::vector<int>& parent,
    int parent_scale,
    int separation,
    int next_scale,
    const std::vector<int>& raw,
    int expected_contamination
) {
    if (v2(separation) % 2 != 0) throw std::runtime_error("wrong sponsor orientation");
    if (raw.size() != 3 * (parent.size() + 1)) throw std::runtime_error("translate layers overlap");
    if (raw.back() >= next_scale) throw std::runtime_error("raw state does not fit next shell");
    verify_left_schedule(parent, separation);

    std::vector<int> centers;
    centers.reserve(parent.size() + 1);
    centers.push_back(separation);
    for (int value : parent) centers.push_back(separation + value);
    std::sort(centers.begin(), centers.end());
    const int minimum = centers.front();
    std::vector<int> fiber;
    for (std::size_t i = 1; i < centers.size(); ++i) fiber.push_back(centers[i] - minimum);
    if (fiber != parent) throw std::runtime_error("middle fiber is not the parent state");

    const std::vector<int> backbone = shell(raw, parent_scale);
    if (!contains_all(backbone, parent)) throw std::runtime_error("backbone loses replay state");
    if (static_cast<int>(backbone.size() - parent.size()) != expected_contamination) {
        throw std::runtime_error("unexpected backbone contamination");
    }
}

std::vector<int> sponsor_candidates(int maximum) {
    std::vector<int> result;
    for (int value = 1; value <= maximum; ++value) if (v2(value) % 2 == 0) result.push_back(value);
    return result;
}

} // namespace

int main() {
    const std::vector<int> s5 = build_s5();
    const std::vector<int> g6 = three_translate_raw(s5, R5);
    const std::vector<int> s6 = translate(g6, L6);
    const std::vector<int> g7 = three_translate_raw(s6, R6);
    const std::vector<int> s7 = translate(g7, L7);

    if (s5.size() != 1092 || s5.front() != L5 || s5.back() != 63668 || fnv_state(s5) != S5_FNV) {
        throw std::runtime_error("S5 mismatch");
    }
    if (g6.size() != 3279 || g6.front() != 0 || g6.back() != 250620 || fnv_state(g6) != G6_FNV) {
        throw std::runtime_error("G6 mismatch");
    }
    if (s6.size() != 3279 || s6.front() != L6 || s6.back() != 512764 || fnv_state(s6) != S6_FNV) {
        throw std::runtime_error("S6 mismatch");
    }
    if (g7.size() != 9840 || g7.front() != 0 || g7.back() != 973092 || fnv_state(g7) != G7_FNV) {
        throw std::runtime_error("G7 mismatch");
    }
    if (s7.size() != 9840 || s7.front() != L7 || s7.back() != 2021668 || fnv_state(s7) != S7_FNV) {
        throw std::runtime_error("S7 mismatch");
    }

    APChecker chain_checker(s7.back());
    if (chain_checker.has_four_ap(g6) || chain_checker.has_four_ap(g7)) {
        throw std::runtime_error("new chain contains a four-term progression");
    }
    verify_replication_step(s5, L5, R5, L6, g6, 0);
    verify_replication_step(s6, L6, R6, L7, g7, 2);

    const int factor_two_scale = 2 * L7;
    const int maximum_r = (factor_two_scale - 1 - s7.back()) / 2;
    if (maximum_r != 37741) throw std::runtime_error("factor-two domain mismatch");
    const std::vector<int> candidates = sponsor_candidates(maximum_r);
    if (candidates.size() != 25161) throw std::runtime_error("factor-two candidate count mismatch");

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

    std::vector<int> disjoint;
    for (int candidate : candidates) {
        if (!difference[candidate] && !difference[2 * candidate]) disjoint.push_back(candidate);
    }
    if (disjoint.size() != 202) throw std::runtime_error("factor-two disjoint count mismatch");

    std::atomic<int> valid_count{0};
#ifdef _OPENMP
#pragma omp parallel
#endif
    {
        APChecker checker(factor_two_scale - 1);
#ifdef _OPENMP
#pragma omp for schedule(dynamic,1)
#endif
        for (std::size_t index = 0; index < disjoint.size(); ++index) {
            const std::vector<int> candidate_raw = three_translate_raw(s7, disjoint[index]);
            if (candidate_raw.size() != 3 * (s7.size() + 1)) continue;
            if (candidate_raw.back() >= factor_two_scale) continue;
            if (!checker.has_four_ap(candidate_raw)) ++valid_count;
        }
    }
    if (valid_count != 0) throw std::runtime_error("unexpected factor-two continuation from S7");

    std::cout << "verified: exact factor-eight recovery R5=93476\n";
    std::cout << "verified: contaminated factor-four continuation R6=230164\n";
    std::cout << "verified: scale pattern 4,8,4,4,8,4\n";
    std::cout << "verified: S7 has no factor-two continuation\n";
    std::cout << "state_sizes=1092,3279,9840\n";
    std::cout << "backbone_contamination=0,2\n";
    std::cout << "weighted_density=273/256,3279/4096,615/512\n";
    std::cout << "weighted_density_growth_S7_over_S5=205/182\n";
    std::cout << "factor2_candidate_count=25161\n";
    std::cout << "factor2_disjoint_count=202\n";
    std::cout << "factor2_valid_count=0\n";
    return 0;
}
