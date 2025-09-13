# https://leetcode.com/problems/intersection-of-two-arrays/description/
from utils.examination import Examiner, Testcase


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersecteds: list[int] = []
        seen: dict[int, int] = {}
        for num in nums1:
            seen[num] = 0
        seen2: dict[int, int] = {}
        for num in nums2:
            if num in seen and not num in seen2:
                seen2[num] = 0
                intersecteds.append(num)
        return intersecteds

def examine()->None:
    Examiner(Solution(), 'intersection').run((
        Testcase(([], []), []),
        Testcase(([1,2,2,1], [2,2]), [2]),
        Testcase(([4,9,5], [9,4,9,8,4]), [9,4]),
    ))