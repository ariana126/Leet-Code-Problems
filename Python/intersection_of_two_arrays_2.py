# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        intersected: list[int] = []

        i: int = 0
        j: int = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersected.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return intersected

def examine() -> None:
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    solution: Solution = Solution()
    output = solution.intersect(nums1, nums2)
    print(output)