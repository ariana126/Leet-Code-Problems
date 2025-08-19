# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return 5 <= version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start: int = 0
        end: int = n
        while start <= end:
            mid = int(((start + end) + ((start + end) & 1)) / 2)
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

    def firstBadVersion1(self, n: int) -> int:
        def binary_search(start: int, end: int) -> int:
            if start > end:
                return start
            mid = int(((start + end) + ((start + end) & 1)) / 2)
            if isBadVersion(mid):
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)
        return binary_search(0, n)
def examine()-> None:
    n: int = 100

    solution = Solution()
    output = solution.firstBadVersion(n)
    print(output)