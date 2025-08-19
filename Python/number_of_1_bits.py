# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
class Solution:
    def hammingWeight(self, n: int) -> int:
        weight: int = 0
        while n > 0:
            if 1 & n:
                weight += 1
            n = n >> 1
        return weight

def examine()-> None:
    print(Solution().hammingWeight(2147483645))