# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        current: int = 0
        k: int = 0
        for i in range(len(nums)):
            if val == nums[i]:
                continue
            nums[current] = nums[i]
            current += 1
            k += 1
        return k

def examine()->None:
    nums: list[int] = [3,2,2,3]
    print(Solution().removeElement(nums, 3))
    print(nums)