# https://leetcode.com/problems/valid-perfect-square/description/
from utils.examination import Examiner, Testcase


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if 1 == num:
            return True
        start: int = 1
        end: int = (num // 2)
        while start <= end:
            mid: int = (start + end) // 2
            square: int = mid * mid
            if num == square:
                return True
            if num > square:
                start = mid + 1
            else:
                end = mid - 1
        return False

def examine()->None:
    Examiner(Solution(), 'isPerfectSquare').run((
        Testcase((1,), True),
        Testcase((4,), True),
        Testcase((9,), True),
        Testcase((16,), True),
        Testcase((1849,), True),
        Testcase((2,), False),
        Testcase((10,), False),
        Testcase((43,), False),
    ))