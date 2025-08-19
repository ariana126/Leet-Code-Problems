# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: list[int]) -> int:
        farest: int = 0
        end_of_window: int = 0
        jump_steps: int = 0
        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if end_of_window == i:
                jump_steps += 1
                end_of_window = farest
                if len(nums) - 1 <= end_of_window:
                    break
        return jump_steps

    def jump2(self, nums: list[int]) -> int:
        map: dict[int, list[int]] = {}
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if len(nums) - 1 < i + j:
                    break
                if not (j + i) in map:
                    map[j + i] = []
                map[i + j].append(i)

        min_jumps: int = 0
        start_position: int = len(nums) - 1
        while 0 != start_position:
            min_jumps += 1
            start_position = map[start_position][0]
        return min_jumps


    def jump2(self, nums: list[int]) -> int:
        map: dict[int, list[int]] = {}
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if len(nums) - 1 < i + j:
                    break
                if not (j + i) in map:
                    map[j + i] = []
                map[i + j].append(i)
        return self.dp_jump(len(nums) - 1, map, {})

    def dp_jump(self, target_index: int, map: dict[int, list[int]], cache: dict[int, int]) -> int:
        if 0 == target_index:
            return 0
        if target_index in cache:
            return cache[target_index]
        min_jump: int = 0xffffffff
        for i in map[target_index]:
            ci: int = self.dp_jump(i, map, cache)
            if min_jump > ci:
                min_jump = ci
        cache[target_index] = min_jump + 1
        return min_jump + 1

def examine()->None:
    input_: list[int] = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    # input_: list[int] = [2,3,1,1,5]

    print(Solution().jump(input_))