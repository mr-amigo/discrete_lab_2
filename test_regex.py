from regex import RegexFSM


def main():
    cases = [
        ("a*4.+hi", [
            ("aaaaaa4uhi", True),
            ("4uhi", True),
            ("meow", False),
        ]),
        ("a+b*", [
            ("", False),
            ("a", True),
            ("aaabb", True),
            ("b", False),
        ]),
        ("H.+", [
            ("H", False),
            ("Hi", True),
            ("Hello", True),
            ("hello", False),
        ]),
    ]

    for pattern, inputs in cases:
        RegexFSM.curr_state.next_states = []
        fsm = RegexFSM(pattern)
        print(f"\n{pattern!r}:")
        for s, expected in inputs:
            got = fsm.check_string(s)
            mark = "OK" if got == expected else "FAIL"
            print(f"  {s!r:>12} -> {got}  [{mark}]")


if __name__ == "__main__":
    main()
