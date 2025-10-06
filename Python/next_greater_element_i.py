# https://leetcode.com/problems/next-greater-element-i/
from utils.examination import Examiner, Testcase


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if 0 == len(nums1) or 0 == len(nums2):
            return []

        geaters: dict[int, int] = {}
        stack: list[int] = []

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                geaters[top] = num
            stack.append(num)
        for num in stack:
            geaters[num] = -1

        sub_graters: list[int] = []
        for num in nums1:
            sub_graters.append(geaters[num])

        return sub_graters

def examine() -> None:
    Examiner(Solution(), 'nextGreaterElement').run((
        Testcase(([4,1,2], [1,3,4,2]), [-1,3,-1]),
        Testcase(([2,4], [1,2,3,4]), [3,-1]),
    ))