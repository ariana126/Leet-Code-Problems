# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits: int = 0
        for i in range(32):
            reversed_bits = reversed_bits << 1
            reversed_bits += 1 & n
            n = n >> 1
        return reversed_bits

def examine() -> None:
    print(Solution().reverseBits(13))