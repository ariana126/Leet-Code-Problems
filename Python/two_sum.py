# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_numbs: dict[int, list[int]] = {}
        for i in range(len(nums)):
            if not (nums[i] in seen_numbs):
                seen_numbs[nums[i]] = []
            seen_numbs[nums[i]].append(i)

        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted not in seen_numbs or (nums[i] == wanted and 2 > len(seen_numbs[wanted])):
                continue
            return [seen_numbs[wanted][len(seen_numbs[wanted]) - 1], i]

        return []


def examine() -> None:
    nums = [3, 6, 2, 3, 3]
    target = 6

    solution = Solution()
    output = solution.twoSum(nums, target)
    print(output)