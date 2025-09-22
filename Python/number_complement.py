# https://leetcode.com/problems/number-complement/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def findComplement(self, num: int) -> int:
        b: int = 0
        i: int = 0
        p: int = 0
        while num >= p:
            b += p
            p = 2 ** i
            i += 1
        return num ^ b


def examine() -> None:
    Examiner(Solution(), 'findComplement').run((
        Testcase((5,), 2),
        Testcase((1,), 0),
    ))