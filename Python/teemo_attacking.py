# https://leetcode.com/problems/teemo-attacking/description/
from utils.examination import Examiner, Testcase


class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int: 


def examine() -> None:
    Examiner(Solution(), 'findPoisonedDuration').run((
        Testcase(([1, 4], 2), 4),
        Testcase(([1, 2], 2), 3),
        Testcase(([1,2,3,4,5], 5), 9),
    ))