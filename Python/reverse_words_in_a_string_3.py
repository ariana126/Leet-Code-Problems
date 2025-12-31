# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start: int = 0
        end: int = 0
        while end <= len(s):
            if end < len(s) and not ' ' == s[end]:
                end += 1
                continue
            end -= 1
            p: int = end
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            end = p + 2
            start = end
        return ''.join(s)

def examine()-> None:
    Examiner(Solution(), 'reverseWords').run((
        Testcase(('',), ''),
        Testcase(('ab',), 'ba'),
        Testcase(('Mr Ding',), 'rM gniD'),
        Testcase(("Let's take LeetCode contest",), "s'teL ekat edoCteeL tsetnoc"),
    ))