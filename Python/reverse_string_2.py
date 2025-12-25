# https://leetcode.com/problems/reverse-string-ii/
from utils.examination import Examiner, Testcase


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i: int = 0
        start: int = 2 * k * i
        end: int = start + k - 1
        while start < len(s):
            if len(s) <= end:
                end = len(s) - 1
            while start < end:
                lst: list = list(s)
                lst[start], lst[end] = lst[end], lst[start]
                s = ''.join(lst)
                start += 1
                end -= 1
            i += 1
            start = 2 * k * i
            end = start + k - 1
        return s




def examine() -> None:
    Examiner(Solution(), 'reverseStr').run((
        Testcase(('abcdefg', 2), 'bacdfeg'),
        Testcase(('abcd', 2), 'bacd'),
        Testcase(('a', 2), 'a'),
        Testcase(('a', 200), 'a'),
    ))