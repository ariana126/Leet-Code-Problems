# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        def swap(x1: int, y1: int, x2: int, y2: int, matrix_: list[list[int]]) -> None:
            matrix_[x1][y1] ^= matrix_[x2][y2]
            matrix_[x2][y2] ^= matrix_[x1][y1]
            matrix_[x1][y1] ^= matrix_[x2][y2]

        length = len(matrix)
        if 1 == length:
            return
        x: int = 0
        l: int = length - 1
        while x < (length - (length & 1)) / 2:
            y: int = x
            while y < l:
                swap(x, y, y, l, matrix)
                swap(x, y, l, l - y + x, matrix)
                swap(x, y, l - y + x, x, matrix)
                y += 1
            x += 1
            l -= 1

def examine() -> None:
    input_: list[list[int]] = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    solution = Solution()
    solution.rotate(input_)
    for matrix in input_:
        print(matrix)