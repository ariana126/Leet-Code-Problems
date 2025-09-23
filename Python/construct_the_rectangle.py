# https://leetcode.com/problems/construct-the-rectangle/

from math import sqrt

from utils.examination import Examiner, Testcase, Logger


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        square: int = int(sqrt(area))
        for i in range(square, 0, -1):
            if 0 == area % i:
                return [area // i, i]

def examine() -> None:
    Examiner(Solution(), 'constructRectangle').run((
        Testcase((4,), [2,2]),
        Testcase((37,), [37,1]),
        Testcase((122122,), [427,286]),
    ))