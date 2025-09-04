# https://leetcode.com/problems/contains-duplicate-ii/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map_: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num not in map_:
                map_[num] = i
                continue
            if k >= i - map_[num]:
                return True
            map_[num] = i
        return False

def examine()->None:
    Examiner(Solution(), 'containsNearbyDuplicate').run((
        Testcase(([1,2,3,1], 3), True),
        Testcase(([1,0,1,1], 1), True),
        Testcase(([1,2,3,1,2,3], 2), False),
    ))