# https://leetcode.com/problems/repeated-substring-pattern/description/
from xdg.Mime import app_exe

from utils.examination import Examiner, Testcase, Logger


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l: int = len(s)
        if 0 == 1 & l and s[:(l // 2)] == s[(l // 2):]:
            return True

        i: int = 0
        if 1 == 1 & l:
            i = 1
        left: int = (l - i) // 2
        right: int = left + i
        while 1 <= left:
            # Logger.log(i, left, right, s[:left], s[right:], s[left:right], s[:i], s[-i:])
            if s[:left] == s[right:] and s[left:right] == s[:i] == s[-i:]:
                return True
            i += 2
            left: int = (l - i) // 2
            right: int = left + i
        return False


def examine() -> None:
    Examiner(Solution(), 'repeatedSubstringPattern').run((
        Testcase(('babba',), False),
        Testcase(('ababab',), True),
        Testcase(('abaaaabaaaabaaa',), True),
        Testcase(('aaa',), True),
        Testcase(('abab',), True),
        Testcase(('aba',), False),
        Testcase(('abcabcabcabc',), True),
        Testcase(('a',), False),
        Testcase(('abaababaab',), True),
    ))