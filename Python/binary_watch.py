# https://leetcode.com/problems/binary-watch/description/
from utils.examination import Examiner, Testcase


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if 8 < turnedOn:
            return []
        possibilities: list[str] = []
        for h in range(12):
            for m in range(60):
                if turnedOn == bin(h).count('1') + bin(m).count('1'):
                    time_: str  = f'{h}:{m}'
                    if 10 > m:
                        time_ = time_[:-1] + '0' + time_[-1:]
                    possibilities.append(time_)
        return possibilities

def examine()-> None:
    Examiner(Solution(), 'readBinaryWatch').run((
        Testcase((9,), []),
        Testcase((0,), []),
        Testcase((1,), ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]),
    ))