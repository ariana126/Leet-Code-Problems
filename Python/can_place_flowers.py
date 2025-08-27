# https://leetcode.com/problems/can-place-flowers/description/
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if 0 == n:
            return True
        i: int = 0
        l: int = len(flowerbed)
        while i < l:
            right: bool = l - 1 == i or 0 == flowerbed[i+1]
            if not right:
                i += 3
                continue
            if 1 == flowerbed[i]:
                i += 2
                continue
            left: bool = 0 == i or 0 == flowerbed[i-1]
            if not left:
                i += 1
                continue
            flowerbed[i] = 1
            n -= 1
            if 0 == n:
                return True
            i += 2
        return 0 >= n

    def canPlaceFlowers1(self, flowerbed: list[int], n: int) -> bool:
        if 0 == n:
            return True
        if 0 == len(flowerbed):
            return False
        def check_neighbours() -> bool:
            left: bool = False
            right: bool = False
            if 0 == i:
                left = True
            else:
                left = 0 == flowerbed[i-1]
            if i == len(flowerbed) - 1:
                right = True
            else:
                right = 0 == flowerbed[i+1]
            return left and right
        for i in range(len(flowerbed)):
            if 1 == flowerbed[i]:
                continue
            if not check_neighbours():
                continue
            flowerbed[i] = 1
            n -= 1
        return n <= 0


def examine():
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1))
    print(Solution().canPlaceFlowers([0, 1, 0, 0, 1], 1))
    print(Solution().canPlaceFlowers([1,0,0,0,0,1], 2))