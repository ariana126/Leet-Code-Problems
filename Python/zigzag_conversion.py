# https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert1(self, s: str, numRows: int) -> str:
        if 1 == numRows or numRows > len(s):
            return s

        sections: list[str] = []
        for i in range(numRows):
            sections.append(s[i])

        pivot: bool = False
        for i in range(numRows, len(s)):
            x: int = ((i + 1) - numRows) % (numRows - 1)
            sec: int
            if pivot:
                if 0 == x:
                    sec = len(sections) - 1
                else:
                    sec = x
            else:
                if 0 == x:
                    sec = 0
                else:
                    sec = len(sections) - 1 - x
            print(i, sec, pivot)
            sections[sec] += s[i]
            if 0 == x:
                pivot = not pivot
        print(sections)
        converted: str = ''
        for sec in sections:
            converted += sec
        return converted

def examine()->None:
    print(Solution().convert("123456789", numRows=3))