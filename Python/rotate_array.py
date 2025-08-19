# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length: int = len(nums)
        if length < k:
            k = k % length
        if 0 == k or length == k:
            return
        pivot: int = length - k
        buf_val: int = nums[0]
        buf_index: int = 0
        loop_index: int = 0
        for i in range(length):
            if pivot > buf_index:
                target_index: int = buf_index + k
            else:
                target_index: int = buf_index + k - length

            nums[target_index], buf_val = buf_val, nums[target_index]
            buf_index = target_index

            if loop_index == buf_index:
                loop_index = loop_index + 1
                buf_index = buf_index + 1
                buf_val = nums[buf_index]

def examine() -> None:
    nums: list[int] = [1, 2, 3]
    k: int = 6

    solution: Solution = Solution()
    solution.rotate(nums, k)

    print(nums)