# https://leetcode.com/problems/power-of-two/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0 >= n:
            return False
        while 1 < n:
            if 1 == n % 2:
                return False
            n = int(n / 2)
        return True

    def isPowerOfTwo1(self, n: int) -> bool:
        if 0 >= n:
            return False
        binary_ones: int = 0
        while 0 < n:
            if n & 1:
                binary_ones += 1
                if 1 < binary_ones:
                    return False
            n = n >> 1
        return True

def examine()->None:
    Examiner(Solution(), 'isPowerOfTwo').run((
        Testcase((1,), True),
        Testcase((16,), True),
        Testcase((3,), False),
    ))