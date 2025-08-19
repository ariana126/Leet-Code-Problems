# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance: int = 0
        n: int = x ^ y
        while 0 < n:
            distance += 1 & n
            n = n >> 1
        return distance

def examine()-> None:
    print(Solution().hammingDistance(1, 3))