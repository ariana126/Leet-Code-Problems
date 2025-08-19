# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i: int = len(digits) - 1
        digits[i] += 1
        while 10 == digits[i]:
            digits[i] = 0
            if 0 == i:
                digits[0] = 1
                for j in range(1, len(digits)):
                    digits[j] = 0
                digits.append(0)
                break

            digits[i - 1] += 1
            i -= 1

        return digits

def examine() -> None:
    input_: list[int] = [9, 9, 9, 2, 9, 9, 9]

    solution = Solution()
    output = solution.plusOne(input_)
    print(output)