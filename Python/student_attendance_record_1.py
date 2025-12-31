# https://leetcode.com/problems/student-attendance-record-i/description/
from enum import StrEnum

from utils.examination import Examiner, Testcase

class Record(StrEnum):
    ABSENT = 'A'
    LATE = 'L'
    PRESENT = 'P'

class Solution:
    def checkRecord(self, s: str) -> bool:
        is_eligible: bool = True
        absent_times: int = 0
        late_times_window: int = 0
        for record in s:
            if Record.ABSENT == record:
                absent_times += 1
                if 1 < absent_times:
                    is_eligible = False
                    break
            if Record.LATE == record:
                late_times_window += 1
                if 2 < late_times_window:
                    is_eligible = False
                    break
            else:
                late_times_window = 0
        return is_eligible

def examine() -> None:
    Examiner(Solution(), 'checkRecord').run((
        Testcase(('PPALLP',), True),
        Testcase(('PPALLL',), False),
    ))