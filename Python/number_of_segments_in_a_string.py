# https://leetcode.com/problems/number-of-segments-in-a-string/description/
from utils.examination import Examiner, Testcase


class Solution:
    def countSegments(self, s: str) -> int:
        segments_count: int = 0
        segment_started: bool = False
        for char in s:
            if ' ' == char:
                if segment_started:
                    segments_count += 1
                    segment_started = False
            else:
                segment_started = True
        if segment_started:
            segments_count += 1
        return segments_count


def examine()->None:
    Examiner(Solution(), 'countSegments').run((
        Testcase(('Hello, my name is John',), 5),
        Testcase((' Hello, my name is John' ,), 5),
        Testcase(('Hello,',), 1),
        Testcase(('',), 0),
        Testcase(('  ',), 0),
        Testcase((' Hello, ',), 1),
    ))