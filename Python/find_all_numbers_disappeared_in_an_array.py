# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
from utils.examination import Examiner, Testcase


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        original_list: list[int] = [i for i in range(1, n + 1)]
        for num in nums:
            original_list[num - 1] = -1
        i: int = 0
        while i < len(original_list):
            if -1 != original_list[i]:
                i += 1
                continue
            del original_list[i]
        return original_list

    def findDisappearedNumbers1(self, nums: list[int]) -> list[int]:
        appeared: dict[int, int] = {}
        for num in nums:
            appeared[num] = 1
        disappeared: list[int] = []
        for i in range(1, len(nums) + 1):
            if i in appeared:
                continue
            disappeared.append(i)
        return disappeared

def examine() -> None:
    Examiner(Solution(), 'findDisappearedNumbers').run((
        Testcase(([4,3,2,7,8,2,3,1],), [5,6]),
        Testcase(([1,1],), [2]),
    ))