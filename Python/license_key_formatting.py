# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        formated: str = ''
        group_count: int = 0
        for i in range(len(s) - 1, -1, -1):
            if '-' == s[i]:
                continue
            if k == group_count:
                group_count = 0
                formated = '-' + formated
            formated = self.__convert_to_uppercase(s[i]) + formated
            group_count += 1
        return formated
    def __convert_to_uppercase(self, s: str) -> str:
        return s.upper()

def examine()-> None:
    s: str = "5F3Z-2e-9-w"
    k: int = 4
    print(Solution().licenseKeyFormatting(s, k))