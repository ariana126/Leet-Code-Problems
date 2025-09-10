# https://leetcode.com/problems/counting-bits/description/
from utils.examination import Examiner, Testcase


class Solution:
    def countBits(self, n: int) -> list[int]:
        bits: list[int] = [0]
        while n + 1 > len(bits):
            i: int = 0
            l: int =  len(bits)
            while n + 1 > len(bits) and l > i:
                bits.append(1 + bits[i])
                i += 1
        return bits


def examine()->None:
    Examiner(Solution(), 'countBits').run((
        Testcase((2,), [0,1,1]),
        Testcase((5,), [0,1,1,2,1,2]),
        Testcase((20,), [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2]),
    ))