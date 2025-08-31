# https://leetcode.com/problems/excel-sheet-column-title/description/
from utils.examination import Examiner, Testcase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if 0 == columnNumber:
            return ''
        first_char: int = columnNumber % 26
        if 0 == first_char:
            first_char = 26
        return self.convertToTitle(int((columnNumber - first_char) / 26)) + chr(64 + first_char)

def examine() -> None:
    Examiner(Solution(), 'convertToTitle').run((
        Testcase((1,), 'A'),
        Testcase((28,), 'AB'),
        Testcase((701,), 'ZY'),
        Testcase((26,), 'Z'),
        Testcase((27,), 'AA'),
        Testcase((52,), 'AZ'),
    ))