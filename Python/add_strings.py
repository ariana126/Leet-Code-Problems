# https://leetcode.com/problems/add-strings/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_i: int = len(num1) - 1
        num2_i: int = len(num2) - 1
        p: int = 0
        sum_: str = ''
        while num1_i >= 0 or num2_i >= 0:
            n1: int = 0
            if 0 <= num1_i:
                n1 = ord(num1[num1_i]) - ord('0')
            n2: int = 0
            if 0 <= num2_i:
                n2 = ord(num2[num2_i]) - ord('0')
            s: int = n1 + n2 + p
            if 10 <= s:
                p = 1
                s = s - 10
            else:
                p = 0
            sum_ = chr(s + ord('0')) + sum_
            num1_i -= 1
            num2_i -= 1
        if 0 < p:
            sum_ = chr(p + ord('0')) + sum_
        return sum_

def examine()-> None:
    Examiner(Solution(), 'addStrings').run((
        Testcase(('11', '123'), '134'),
        Testcase(('456', '77'), '533'),
        Testcase(('0', '0'), '0'),
        Testcase(('32', '0'), '32'),
        Testcase(('999', '1'), '1000'),
    ))