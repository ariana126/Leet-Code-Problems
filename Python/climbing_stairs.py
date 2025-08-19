# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if 1 == n:
            return 1
        if 2 == n:
            return 2
        one_before: int = 2
        two_before: int = 1
        for i in range(3, n):
            t1: int = one_before
            one_before += two_before
            two_before = t1
        return one_before + two_before

    def climbStairs2(self, n: int) -> int:
        cache: dict[int, int] = {}
        cache[1] = 1
        cache[2] = 2

        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]

    def climbStairs1(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if 1 == n:
            return 1
        if 2 == n:
            return 2
        r: int = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = r
        return r

def examine()-> None:
    n: int = 50

    output = Solution().climbStairs(n)
    print(output)