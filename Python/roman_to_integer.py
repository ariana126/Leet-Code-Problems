# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        integer: int = 0
        i: int = len(s) - 1
        while -1 < i:
            c: str = s[i - 1] + s[i]
            if 0 < i and c in dictionary:
                integer += dictionary[c]
                i -= 2
                continue
            integer += dictionary[s[i]]
            i -= 1

        return integer

def examine()-> None:
    print(Solution().romanToInt('MCMXCIV'))