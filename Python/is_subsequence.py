# https://leetcode.com/problems/is-subsequence/description/
from utils.examination import Examiner, Testcase


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        s_i: int = 0
        t_i: int = 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1
        return s_i >= len(s)

def examine()->None:
    Examiner(Solution(), 'isSubsequence').run((
        Testcase(('', ''), True),
        Testcase(('A', 'c'), False),
        Testcase(('abc', 'ahbgdc'), True),
        Testcase(('axc', 'ahbgdc'), False),
    ))