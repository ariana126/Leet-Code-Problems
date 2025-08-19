# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        tree: list[list[int]] = [[1]]
        for i in range(1, numRows):
            new_row: list[int] = []
            for j in range(i + 1):
                if 0 == j or i == j:
                    new_row.append(1)
                    continue
                new_row.append(tree[i - 1][j - 1] + tree[i - 1][j])
            tree.append(new_row)
        return tree

def examine()-> None:
    input_: int = 5
    output_ = Solution().generate(input_)
    print(output_)