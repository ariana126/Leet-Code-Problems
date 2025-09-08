# https://leetcode.com/problems/summary-ranges/
from utils.examination import Examiner, Testcase


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if 0 == len(nums):
            return []
        summary: list[str] = []
        a: int = 0
        b: int = 0
        for i in range(1, len(nums)):
            if nums[b] == nums[i] - 1:
                b += 1
                continue
            if a == b:
                summary.append(str(nums[a]))
            else:
                summary.append(f'{nums[a]}->{nums[b]}')
            b += 1
            a = b
        if a == b:
            summary.append(str(nums[a]))
        else:
            summary.append(f'{nums[a]}->{nums[b]}')
        return summary

def examine()->None:
    Examiner(Solution(), 'summaryRanges').run((
        Testcase(([0,1,2,4,5,7],), ["0->2","4->5","7"]),
        Testcase(([0,2,3,4,6,8,9],), ["0","2->4","6","8->9"]),
    ))