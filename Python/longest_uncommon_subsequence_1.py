# https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
from utils.examination import Examiner, Testcase


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))

def examine()->None:
    Examiner(Solution(), 'findLUSlength').run((
        Testcase(('aba', 'cdc'), 3),
        Testcase(('aaa', 'bbb'), 3),
        Testcase(('aac', 'bbc'), 3),
        Testcase(('aca', 'bcb'), 3),
        Testcase(('aaa', 'a'), 3),
        Testcase(('aaa', 'aaa'), -1),
    ))