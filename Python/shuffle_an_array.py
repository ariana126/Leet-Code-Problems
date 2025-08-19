# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
import random


class Solution:
    def __init__(self, nums: list[int]):
        self._nums = nums
    def reset(self) -> list[int]:
        return self._nums.copy()

    def shuffle(self) -> list[int]:
        if 2 > len(self._nums):
            return self.reset()

        shuffled: list[int] = []
        map_: list[int] = self._nums.copy()
        for i, num in enumerate(map_):
            position = random.randint(i, len(self._nums) - 1)
            shuffled.append(map_[position])
            map_[position] = map_[i]

        return shuffled


def examine()-> None:
    nums = [1, 2, 3, 4]
    nums = [-6, 10, 184]

    obj = Solution(nums)
    print(obj.shuffle())
    print(obj.reset())
    print(obj.shuffle())
