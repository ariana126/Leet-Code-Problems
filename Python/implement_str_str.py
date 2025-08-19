# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if 0 == len(needle):
            return -1

        needle_dic: dict[str, list[int]] = {}
        for i, char in enumerate(needle):
            if char not in needle_dic:
                needle_dic[char] = []
            needle_dic[char].append(i)
        haystack_dic: dict[str, list[int]] = {}
        for i, char in enumerate(haystack):
            if char not in haystack_dic:
                haystack_dic[char] = []
            haystack_dic[char].append(i)
        for c, indexes in needle_dic.items():
            if c not in haystack_dic:
                return -1
            if len(indexes) > len(haystack_dic[c]):
                return -1

        for i in haystack_dic[needle[0]]:
            if len(haystack) - i < len(needle):
                break
            matches: bool = True
            for j in range(1, len(needle)):
                if haystack[j + i] != needle[j]:
                    matches = False
                    break
            if not matches:
                continue
            return i
        return -1

def examine()->None:
    haystack = "mississippi"
    needle = 'issipi'

    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)