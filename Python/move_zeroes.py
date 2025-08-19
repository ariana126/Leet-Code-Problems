# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j: int = 0
        for i in range(len(nums)):
            if 0 != nums[i]:
                if j == i:
                    j += 1
                    continue
                nums[j] = nums[i]
                nums[i] = 0
                j += 1

def examine() -> None:
    input_: list[int] = [2]

    solution = Solution()
    solution.moveZeroes(input_)
    print(input_)
