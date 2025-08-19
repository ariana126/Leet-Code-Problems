# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        smallest: int = prices[0]
        max_profit: int  = 0
        for i in range(1, len(prices)):
            if smallest > prices[i]:
                smallest = prices[i]
                continue
            if max_profit < prices[i] - smallest:
                max_profit = prices[i] - smallest

        return max_profit

def examine()-> None:
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))