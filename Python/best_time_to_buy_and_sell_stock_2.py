# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit: int = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]

        return max_profit

def examine():
    solution: Solution = Solution()

    prices: list[int] = [7,6,4,3,1]
    output: int = solution.maxProfit(prices)

    print(output)