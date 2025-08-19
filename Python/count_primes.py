# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
class Solution:
    def countPrimes(self, n: int) -> int:
        nums: dict[int, bool] = {}
        for i in range(2, n):
            if i in nums:
                continue
            for j in range(i * i, n, i):
                nums[j] = False
        count: int = 0
        for i in range(2, n):
            if not i in nums:
                count += 1
        return count

def examine()->None:
    print(Solution().countPrimes(10))