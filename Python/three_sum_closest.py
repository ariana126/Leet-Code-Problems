# https://leetcode.com/problems/3sum-closest/description/
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diffs: list[int] = []
        for num in nums:
            diffs.append(target - num)
        diffs.sort()
        print(diffs)
        return target - diffs[0] - diffs[1] - diffs[2]

        nums.sort()
        min_sum: int = 0
        selected_nums: list[int] = []
        for i in range(3):
            min_sum += nums[i]
            selected_nums.append(nums[i])

        for i in range(3, len(nums)):
            print(selected_nums, min_sum)
            diff: int = self._diff(target, min_sum)
            if 0 == diff:
                return target

            diff1: int = self._diff(target, selected_nums[1] + selected_nums[2] + nums[i])
            diff2: int = self._diff(target, selected_nums[0] + selected_nums[2] + nums[i])
            diff3: int = self._diff(target, selected_nums[0] + selected_nums[1] + nums[i])
            print(diff, diff1, diff2, diff3)
            if diff1 < diff and diff1 <= diff2 and diff1 <= diff3:
                selected_nums[0] = nums[i]
                min_sum = selected_nums[1] + selected_nums[2] + nums[i]
                continue
            if diff2 < diff and diff2 <= diff1 and diff2 <= diff3:
                selected_nums[1] = nums[i]
                min_sum = selected_nums[0] + selected_nums[2] + nums[i]
                continue
            if diff3 < diff and diff3 <= diff2 and diff3 <= diff1:
                selected_nums[2] = nums[i]
                min_sum = selected_nums[0] + selected_nums[1] + nums[i]
                continue

        return min_sum

    def _diff(self, num1: int, num2: int) -> int:
        return abs(num1 - num2)

def examine()->None:
    # nums: list[int] = [10, 0, -1, 2, 1, -4]
    nums: list[int] = [5, 0, 0, -2, 1, -10]
    nums: list[int] = [1,1,1,5,5,5,5,5,5]
    nums: list[int] = [1, 1, 1, 0]
    # nums: list[int] = [-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]
    target: int = 1

    print(Solution().threeSumClosest(nums, target))