class Solution:
    def canWinNim(self, n: int) -> bool:
        return not 0 == n % 4

def examine() -> None:
    print(Solution().canWinNim(4))