# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        m -= 1
        n -= 1
        for i in range(m + n + 1    , -1, -1):
            if -1 == n:
                break
            if nums2[n] > nums1[m] or -1 == m:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1

def examine()-> None:
    nums1 = [1, 2, 3]
    nums2 = []

    solution = Solution()
    solution.merge(nums1, 3, nums2, 0)
    print(nums1)