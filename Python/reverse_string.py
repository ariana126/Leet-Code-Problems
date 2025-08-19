# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
class Solution:
    def reverseString(self, s: list[str]) -> None:
        start: int = 0
        end: int = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

def examine() -> None:
    input_: list[str] = ["H","a","n","n","a","h"]

    solution = Solution()
    solution.reverseString(input_)
    print(input_)
