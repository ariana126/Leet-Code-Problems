# https://leetcode.com/problems/ugly-number/description/
from utils.examination import Examiner, Testcase


class Solution:
    def isUgly(self, n: int) -> bool:
        if 0 >= n:
            return False
        while 1 < n:
            if 0 == n % 2:
                n = int(n / 2)
                continue
            if 0 == n % 3:
                n = int(n / 3)
                continue
            if 0 == n % 5:
                n = int(n / 5)
                continue
            return False
        return True

def examine()->None:
    Examiner(Solution(), 'isUgly').run((
        Testcase((6,), True),
        Testcase((1,), True),
        Testcase((14,), False),
    ))