# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing: int = 0
        for i in range(len(nums) + 1):
            missing ^= i
        for num in nums:
            missing ^= num
        return missing

    def missingNumber1(self, nums: list[int]) -> int:
        valid_sum: int = 0
        for i in range(len(nums) + 1):
            valid_sum += i
        sum_of_nums: int = 0
        for num in nums:
            sum_of_nums += num
        return valid_sum - sum_of_nums

def examine()->None:
    nums = [1, 3, 0]
    print(Solution().missingNumber(nums))