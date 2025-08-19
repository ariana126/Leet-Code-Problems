# https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_: str = ''

        p: int = 0
        al: int = len(a) - 1
        bl: int = len(b) - 1
        remaining: int = 0
        while al >= p or bl >= p:
            if al < p:
                an: int = 0
            else:
                an: int = int(a[al - p])
            if bl < p:
                bn: int = 0
            else:
                bn: int = int(b[bl - p])

            digit: int = an + bn + remaining
            remaining = 0
            if 2 <= digit:
                remaining = 1
                digit -= 2
            p += 1
            sum_ = str(digit) + sum_
        if 0 < remaining:
            sum_ = str(remaining) + sum_

        return sum_

def examine()-> None:
    print(Solution().addBinary('11', '100'))