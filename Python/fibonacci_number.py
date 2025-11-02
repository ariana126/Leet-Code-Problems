# https://leetcode.com/problems/fibonacci-number/description/
from utils.examination import Examiner, Testcase


class Solution:
    def fib(self, n: int) -> int:
        one: int = 0
        two: int = 1
        for _ in range(n):
            one, two = two, one + two
        return one


def examine()-> None:
    Examiner(Solution(), 'fib').run((
        Testcase((0,), 0),
        Testcase((1,), 1),
        Testcase((2,), 1),
        Testcase((3,), 2),
        Testcase((4,), 3),
    ))