class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        seen: dict[str, bool] = {}
        first_land_loc: list[int] = self.find_first_land(grid)
        return self.travel_dp(grid, first_land_loc[0], first_land_loc[1], seen)

    def mark_seen(self, row: int, col: int, seen: dict[str, bool]) -> None:
        key: str = str(row) + '-' + str(col)
        seen[key] = True
    def has_seen(self, row: int, col: int, seen: dict[str, bool]) -> bool:
        key: str = str(row) + '-' + str(col)
        return key in seen

    def travel_dp(self, grid: list[list[int]], row: int, col: int, seen: dict[str, bool]) -> int:
        if not self.is_cell_full(grid, row, col) or self.has_seen(row, col, seen):
            return 0
        self.mark_seen(row, col, seen)
        perimeter: int = 0
        if not self.is_cell_full(grid, row + 1, col):
            perimeter += 1
        else:
            perimeter += self.travel_dp(grid, row + 1, col, seen)
        if not self.is_cell_full(grid, row - 1, col):
            perimeter += 1
        else:
            perimeter += self.travel_dp(grid, row - 1, col, seen)
        if not self.is_cell_full(grid, row, col + 1):
            perimeter += 1
        else:
            perimeter += self.travel_dp(grid, row, col + 1, seen)
        if not self.is_cell_full(grid, row, col - 1):
            perimeter += 1
        else:
            perimeter += self.travel_dp(grid, row, col - 1, seen)

        return perimeter

    def find_first_land(self, grid: list[list[int]]) -> list[int]:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if 1 == grid[row][col]:
                    return [row, col]
        return [0, 0]

    def is_cell_full(self, grid: list[list[int]], row: int, col: int) -> bool:
        if 0 > row or 0 > col or len(grid) <= row or len(grid[row]) <= col:
            return False
        return 1 == grid[row][col]

    def islandPerimeter1(self, grid: list[list[int]]) -> int:
        perimeter: int = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if 0 == grid[row][col]:
                    continue
                if not self.is_cell_full(grid, row + 1, col):
                    perimeter += 1
                if not self.is_cell_full(grid, row - 1, col):
                    perimeter += 1
                if not self.is_cell_full(grid, row, col + 1):
                    perimeter += 1
                if not self.is_cell_full(grid, row, col - 1):
                    perimeter += 1
        return perimeter

def examine() -> None:
    map: list[list[int]] = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    # map: list[list[int]] = [[1, 0]]
    print(Solution().islandPerimeter(map))