# https://leetcode.com/problems/longest-palindrome/description/
from utils.examination import Examiner, Testcase


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if '' == s:
            return 0
        d: dict[str, int] = {}
        l: int = 0
        for c in s:
            if c not in d:
                d[c] = 1
                continue
            d[c] += 1
            if 2 == d[c]:
                l += 2
                d[c] = 0
        for k, v in d.items():
            if 1 <= v:
                l += 1
                break
        return l

def examine()->None:
    Examiner(Solution(), 'longestPalindrome').run((
        Testcase(('',), 0),
        Testcase(('a',), 1),
        Testcase(('abccccdd',), 7),
    ))