# https://leetcode.com/problems/power-of-four/description/
from utils.examination import Examiner, Testcase


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if 0 >= n:
            return False
        if 1 == n:
            return True
        while 1 < n:
            if 0 != n % 4:
                return False
            n = int(n / 4)
        return True

def examine()->None:
    Examiner(Solution(), 'isPowerOfFour').run((
        Testcase((16,), True),
        Testcase((1,), True),
        Testcase((5,), False),
    ))