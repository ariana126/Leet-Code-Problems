# 
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#     return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        start: int = 0
        end: int = n
        while start <= end:
            mid: int = start + (end - start) // 2
            guessed: int = guess(mid)
            if 0 == guessed:
                return mid
            if -1 == guessed:
                end = mid - 1
            else:
                start = mid + 1
