# https://leetcode.com/problems/arranging-coins/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def arrangeCoins(self, n: int) -> int:
        t: int = 0
        for i in range(1, n + 1):
            t += i
            if t > n:
                return i - 1
            if t == n:
                return i

def examine() -> None:
    Examiner(Solution(), 'arrangeCoins').run((
        Testcase((1,), 1),
        Testcase((2,), 1),
        Testcase((5,), 2),
        Testcase((6,), 3),
        Testcase((8,), 3),
        Testcase((10,), 4),
    ))