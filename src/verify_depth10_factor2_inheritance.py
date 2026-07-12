#!/usr/bin/env python3
"""Verify the geometric inheritance reducing S10 factor two to S9 factor four."""

L8 = 8_388_608
L9 = 67_108_864
L10 = 536_870_912
R8 = 16_777_217
R9 = 134_217_729
S9_MAX = 115_267_902
S10_MAX = 920_574_272


def raw(state, separation):
    anchor = {0} | set(state)
    return {
        value + layer * separation
        for value in anchor
        for layer in range(3)
    }


def translate(state, offset):
    return {offset + value for value in state}


def build_s8():
    h = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    state = {64 + value for value in h}
    for scale, separation in (
        (256, 61),
        (2048, 303),
        (8192, 1597),
        (32768, 8195),
        (262144, 93476),
        (1048576, 230164),
        (L8, 2097164),
    ):
        state = translate(raw(state, separation), scale)
    return state


def main():
    s8 = build_s8()
    s9 = translate(raw(s8, R8), L9)
    s10 = translate(raw(s9, R9), L10)

    if len(s9) != 88_572 or min(s9) != L9 or max(s9) != S9_MAX:
        raise AssertionError("S9 reconstruction mismatch")
    if len(s10) != 265_719 or min(s10) != L10 or max(s10) != S10_MAX:
        raise AssertionError("S10 reconstruction mismatch")

    a9 = {0} | s9
    embedded = translate(a9, L10)
    if not embedded <= s10:
        raise AssertionError("translated A9 is not contained in S10")

    max_r_s9_factor4 = (4 * L9 - 1 - S9_MAX) // 2
    max_r_s10_factor2 = (2 * L10 - 1 - S10_MAX) // 2
    if max_r_s9_factor4 != 76_583_776:
        raise AssertionError("unexpected S9 factor-four endpoint")
    if max_r_s10_factor2 != 76_583_775:
        raise AssertionError("unexpected S10 factor-two endpoint")
    if max_r_s10_factor2 > max_r_s9_factor4:
        raise AssertionError("factor-two domain is not inherited")

    # For every R, translating the complete S9 candidate by L10 gives a
    # subset of the S10 candidate. This identity is checked symbolically on
    # the embedded anchor set and does not require iterating the finite domain.
    test_r = (1, 2035, max_r_s10_factor2)
    for separation in test_r:
        left = translate(raw(s9, separation), L10)
        right = raw(s10, separation)
        if not left <= right:
            raise AssertionError("candidate-containment identity failed")

    print("verified: L10 + ({0} union S9) is contained in S10")
    print("S9_factor4_max_R=76583776")
    print("S10_factor2_max_R=76583775")
    print("verified: every S10 factor-two candidate contains a translated S9 factor-four candidate")
    print("consequence_with_certified_N_9_4_zero: N_10_2=0")


if __name__ == "__main__":
    main()
