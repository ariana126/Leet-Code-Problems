# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive: int = 0
        current: int = 0
        for num in nums:
            if 1 == num:
                current += 1
            else:
                max_consecutive = max(max_consecutive, current)
                current = 0
        return max(max_consecutive, current)

def examine()->None:
    nums: list[int] = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))