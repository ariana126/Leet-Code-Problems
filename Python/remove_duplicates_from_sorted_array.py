# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
            current_max_number: int = nums[0]
            current_index: int = 1
            k: int = 1

            for i in range(1, len(nums)):
                value: int = nums[i]
                if current_max_number < value:
                    if current_index != i:
                        nums[current_index] = value
                    current_index += 1
                    current_max_number = value
                    k += 1

            return k

def examine():
        nums: list[int] = [1, 2, 3, 4, 4, 6]
        solution: Solution = Solution()

        output: int = solution.removeDuplicates(nums)

        print(output)
        print(nums)