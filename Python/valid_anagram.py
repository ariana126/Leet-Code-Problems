# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_numbers: dict = {}
        for c in s:
            if c in seen_numbers:
                seen_numbers[c] += 1
                continue
            seen_numbers[c] = 1
        for c in t:
            if not c in seen_numbers:
                return False
            seen_numbers[c] -= 1
            if 0 > seen_numbers[c]:
                return False
        return True


def examine()-> None:
    s: str = ''
    t: str = ''

    solution = Solution()
    output = solution.isAnagram(s, t)
    print(output)