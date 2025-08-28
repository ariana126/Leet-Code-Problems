# https://leetcode.com/problems/perfect-number/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if 1 == num:
            return False
        i: int = 2
        max_: int = num
        sum_: int = 1
        while max_ > i:
            if 0 == num % i:
                sum_ += i + num // i
                if sum_ > num:
                    return False
                max_ = num // i
            i += 1
        return sum_ == num
def examine()->None:
    Examiner(Solution(), 'checkPerfectNumber').run((
        Testcase((28,), True),
        Testcase((1,), False),
        Testcase((2,), False),
        Testcase((7,), False),
    ))