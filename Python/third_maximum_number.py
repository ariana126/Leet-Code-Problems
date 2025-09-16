# https://leetcode.com/problems/third-maximum-number/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if 1 == len(nums):
            return nums[0]
        if 2 == len(nums):
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        smallest: int = -2 ** 31 - 1
        tops: list[int] = [smallest, smallest, smallest]
        tops.sort()
        for num in nums:
            if num <= tops[0]:
                continue
            if num < tops[1]:
                tops[0] = num
                continue
            if num == tops[1]:
                continue
            if num < tops[2]:
                tops[0] = tops[1]
                tops[1] = num
                continue
            if num == tops[2]:
                continue
            tops[0] = tops[1]
            tops[1] = tops[2]
            tops[2] = num
        if smallest == tops[0]:
            return tops[2]
        else:
            return tops[0]

def examine()->None:
    Examiner(Solution(), 'thirdMax').run((
        Testcase(([2, 3, 1],), 1),
        Testcase(([2, 1],), 2),
        Testcase(([1, 1, 2],), 2),
        Testcase(([2, 1, 2, 3],), 1),
    ))