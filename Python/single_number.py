# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_number: int = 0
        for num in nums:
            unique_number ^= num
        return unique_number

def examine() -> None:
    input_: list[int] = [1, 1, 2, 2, 4, 4, 6]

    solution = Solution()
    output = solution.singleNumber(input_)
    print(output)