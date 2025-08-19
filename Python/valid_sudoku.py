# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        locs: dict[str, list[tuple[int, int]]] = {}
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if '.' == col:
                    continue
                if not col in locs:
                    locs[col] = []

                for loc in locs[col]:
                    if (i == loc[0] or j == loc[1] or
                            (3 > (i ^ loc[0]).bit_count() and 3 > (j ^ loc[1]).bit_count() and
                             (i - (i % 3) == loc[0] - (loc[0] % 3) and j - (j % 3) == loc[1] - (loc[1] % 3))
                            )
                    ):

                        return False

                locs[col].append((i, j))

        return True



def examine() -> None:
    inpt_: list[list[str]] = [["5","3",".",".","7",".",".",".","."]
,["6",".","5","1","9",".",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    solution = Solution()
    output = solution.isValidSudoku(inpt_)
    print(output)