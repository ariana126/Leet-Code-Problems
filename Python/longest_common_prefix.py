# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        if 1 == len(strs):
            return strs[0]
        smallest_string: str = strs[0]
        for s in strs:
            if len(smallest_string) > len(s):
                smallest_string = s

        for i in range(len(smallest_string)):
            for j in range(len(strs)):
                if smallest_string[i] != strs[j][i]:
                    return smallest_string[:i]
            if i == len(smallest_string) - 1:
                return smallest_string
        return ''

def examine()->None:
    strs = ["a", "ab"]

    solution = Solution()
    output = solution.longestCommonPrefix(strs)
    print(output)