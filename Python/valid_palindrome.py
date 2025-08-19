# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated_s: str = ""
        for c in s:
            ascii_code = ord(c)
            if ord('a') <= ascii_code <= ord('z'):
                formated_s += c
            if ord('A') <= ascii_code <= ord('Z'):
                formated_s += chr(ascii_code + (ord('a') - ord('A')))
            if ord('0') <= ascii_code <= ord('9'):
                formated_s += c
        start = 0
        end = len(formated_s) - 1
        while start < end:
            if formated_s[start] != formated_s[end]:
                return False
            start += 1
            end -= 1
        return True

def examine()-> None:
    s: str = "0P"

    solution = Solution()
    output = solution.isPalindrome(s)
    print(output)