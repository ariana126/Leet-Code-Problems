# https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if 2 > len(nums):
            return True
        farest: int = 0
        end_of_window: int = 0
        jump_steps: int = 0
        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if end_of_window == i:
                jump_steps += 1
                end_of_window = farest
                if len(nums) - 1 <= end_of_window:
                    return True
        return False

def examine()->None:
    # input_: list[int] = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    # input_: list[int] = [3,2,1,0,4]
    # input_: list[int] = [2,3,1,1,5]
    input_: list[int] = [0, 1]

    print(Solution().canJump(input_))