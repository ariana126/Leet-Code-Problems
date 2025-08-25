# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_to_p: dict = {}
        p_to_s: dict = {}
        p_index: int = 0
        s_index: int = 0
        while p_index < len(pattern) and s_index < len(s):
            if ' ' == s[s_index]:
                s_index += 1
                continue
            word: str = ''
            while s_index < len(s) and ' ' != s[s_index]:
                word += s[s_index]
                s_index += 1
            p: str = pattern[p_index]
            if p not in p_to_s:
                p_to_s[p] = word
            if word not in s_to_p:
                s_to_p[word] = p
            if not word == p_to_s[p] or not p == s_to_p[word]: 
                return False
            p_index += 1
            s_index += 1
        return p_index >= len(pattern) and s_index > len(s)

def examine()->None:
    pattern: str = 'abbaa'
    s: str = 'dog cat cat dog'
    print(Solution().wordPattern(pattern, s))