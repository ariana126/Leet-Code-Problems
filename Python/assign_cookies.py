# https://leetcode.com/problems/assign-cookies/description/
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        children_index: int = 0
        cookies_index: int = 0
        while cookies_index < len(s) and children_index < len(g):
            if s[cookies_index] < g[children_index]:
                cookies_index += 1
                continue
            children_index += 1
            cookies_index += 1
        return children_index

def examine()->None:
    g: list[int] = [10,9,8,7]
    s: list[int] = [5,6,7,8]
    print(Solution().findContentChildren(g, s))