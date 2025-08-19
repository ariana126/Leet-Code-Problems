# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if 0 >= n or 2 == n:
            return False
        if 1 == n:
            return True
        while n > 1:
            if not 0 == n % 3:
                return False
            n = n / 3
        return True


def examine()-> None:
    print(Solution().isPowerOfThree(-1))