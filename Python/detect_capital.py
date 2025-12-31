# https://leetcode.com/problems/detect-capital/description/
from utils.examination import Examiner, Testcase


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 2 > len(word):
            return True
        if word[0].islower() and not word[1].islower():
            return False
        is_lower: bool = word[1].islower()
        for i in range(2, len(word)):
            if not word[i].islower() == is_lower:
                return False
        return True

def examine() -> None:
    Examiner(Solution(), 'detectCapitalUse').run((
        Testcase(('',), True),
        Testcase(('g',), True),
        Testcase(('gg',), True),
        Testcase(('G',), True),
        Testcase(('USA',), True),
        Testcase(('leetcode',), True),
        Testcase(('Google',), True),
        Testcase(('gG',), False),
        Testcase(('FlaG',), False),
        Testcase(('flaG',), False),
    ))