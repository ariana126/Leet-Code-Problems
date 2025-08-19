# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
from string import whitespace


class Solution:
    def myAtoi(self, s: str) -> int:
        def is_digit(char: str) -> bool:
            return ord('0') <= ord(char) <= ord('9')

        sign: int = 1
        integer: int = 0
        has_explicit_sign_seen: bool = False
        whitespace_skipped: bool = False
        for i, c in enumerate(s):
            if not whitespace_skipped and ' ' == c:
                continue
            whitespace_skipped = True
            if not has_explicit_sign_seen:
                if '-' == c:
                    sign = -1
                    has_explicit_sign_seen = True
                    continue
                elif '+' == c:
                    has_explicit_sign_seen = True
                    continue
            has_explicit_sign_seen = True

            if not is_digit(c):
                return sign * integer

            digit: int = ord(c) - ord('0')
            if 1 == sign:
                max_: int = 2 ** 31 - 1
            else:
                max_: int = 2 ** 31
            if (max_ - digit) / 10 <= integer:
                if 1 == sign:
                    return 2 ** 31 - 1
                else:
                    return -1 * 2 ** 31

            integer = integer * 10 + digit

        return sign * integer


def examine()-> None:
    s: str = "          +-132-337c0d3"

    solution = Solution()
    output = solution.myAtoi(s)
    print(output)