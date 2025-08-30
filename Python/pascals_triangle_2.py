# https://leetcode.com/problems/pascals-triangle-ii/description/
from utils.examination import Examiner, Testcase


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        current_row: list[int] = [1]
        next_row: list[int] = []
        for i in range(1, rowIndex + 1):
            next_row.append(1)
            for j in range(0, len(current_row) - 1):
                next_row.append(current_row[j] + current_row[j + 1])
            next_row.append(1)
            current_row = next_row
            next_row = []
        return current_row

def examine()->None:
    Examiner(Solution(), 'getRow').run((
        Testcase((3,), [1,3,3,1]),
        Testcase((0,), [1]),
        Testcase((1,), [1,1]),
    ))