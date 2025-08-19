# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result: int = 0

        number_of_digits: int = 1
        while x != x % (10 ** number_of_digits):
            number_of_digits += 1

        for position in range(1, number_of_digits + 1):
            current_position: int = int(10 ** position)
            previous_position: int = int(current_position / 10)

            digit: int = int((x % current_position - x % previous_position) / previous_position)

            result += digit * (10 ** (number_of_digits - position))

        if 2 ** 31 - 1 < result or (-1 == sign and 2 ** 31 < result):
            return 0
        return result * sign

    def reverse2(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        s: list[str] = list(str(x))
        start: int = 0
        end: int = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        x = int(''.join(s))
        if 2 ** 31 - 1 < x or (-1 == sign and 2 ** 31 < x):
            return 0
        return x * sign

    def reverse1(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        number_of_digits: int = 1
        while x != x % (10 ** number_of_digits):
            number_of_digits += 1

        for i in range(number_of_digits - 1):
            for position in range(1, number_of_digits - i):
                current_position: int = int(10 ** position)
                previous_position: int = int(current_position / 10)
                next_position: int = int(current_position * 10)

                digit: int = int((x % current_position - x % previous_position) / previous_position)
                next_digit: int = int((x % next_position - x % current_position) / current_position)

                x += (digit - next_digit) * previous_position * 9

        if 2 ** 31 - 1 < x or (-1 == sign and 2 ** 31 < x):
            return 0
        return x * sign

def examine() -> None:
    # x: int = 1534236469
    x: int = 987

    solution = Solution()
    output: int = solution.reverse(x)
    print(output)