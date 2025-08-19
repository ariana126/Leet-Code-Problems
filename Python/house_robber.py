# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
class Solution:
    def rob(self, nums: list[int]) -> int:
        odd_memo: int = 0
        even_memo: int = 0
        max_rob: int = 0
        for i, num in enumerate(nums):
            if not i & 1:
                max_rob = max(max_rob, odd_memo + num)
                odd_memo = max(odd_memo + num, even_memo)
            else:
                max_rob = max(max_rob, even_memo + num)
                even_memo = max(even_memo + num, odd_memo)

        return max_rob

def examine()-> None:
    nums = [3, 1, 2, 10]
    # nums = [1, 2, 3, 4]
    # nums = [2,7,9,3,1]
    output = Solution().rob(nums)
    print(output)