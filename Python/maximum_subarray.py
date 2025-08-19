# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
from yt_dlp.compat import compat_urllib_request


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        compressed: list[int] = [nums[0]]
        positive_section: bool = 0 < nums[0]
        for i in range(1, len(nums)):
            if not (0 < nums[i]) == positive_section:
                positive_section = 0 < nums[i]
                compressed.append(nums[i])
                continue
            compressed[len(compressed) - 1] += nums[i]

        if 1 == len(compressed) and (0 >= nums[0]):
            max_sum: int = nums[0]
            for i in range(1, len(nums)):
                max_sum = max(max_sum, nums[i])
            return max_sum

        i: int = 0
        if 0 >= compressed[i]:
            i += 1
        max_sum: int = 0
        current_block_max_sum: int = 0
        while i < len(compressed):
            current_block_max_sum += compressed[i]
            if len(compressed) - 1 < i + 2:
                max_sum = max(max_sum, current_block_max_sum)
                break
            if not 0 == i and not 1 == i and not 0 == current_block_max_sum:
                current_block_max_sum += compressed[i - 1]

            if current_block_max_sum < abs(compressed[i + 1]):
                max_sum = max(max_sum, current_block_max_sum)
                current_block_max_sum = 0
                i += 2
        return max_sum


def examine()-> None:
    nums = [5, 0, 4,-1,7,8]
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [10, -5, 3, -1, 9]
    print(Solution().maxSubArray(nums))