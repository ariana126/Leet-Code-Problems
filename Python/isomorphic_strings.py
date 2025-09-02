# https://leetcode.com/problems/isomorphic-strings/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}
        for i in range(len(s)):
            if s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            if s[i] not in s_to_t or t[i] not in t_to_s:
                return False
            if s[i] != t_to_s[t[i]]:
                return False
        return True

def examine()->None:
    Examiner(Solution(), 'isIsomorphic').run((
        Testcase(('paper', 'title'), True),
        Testcase(('egg', 'add'), True),
        Testcase(('egg', 'adda'), False),
        Testcase(('egg', 'addb'), False),
        Testcase(('egg', 'ad'), False),
        Testcase(('eg', 'add'), False),
        Testcase(('ege', 'add'), False),
        Testcase(('eggp', 'add'), False),
    ))