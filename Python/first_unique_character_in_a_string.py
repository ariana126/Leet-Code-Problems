# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_numbers: dict = {}
        for i, c in enumerate(s):
            if c in seen_numbers:
                seen_numbers[c] += 1
                continue
            seen_numbers[c] = 1
        for i, c in enumerate(s):
            if 1 == seen_numbers[c]:
                return i
        return -1

def examine() -> None:
    s: str = 'abcd'

    solution = Solution()
    result = solution.firstUniqChar(s)
    print(result)