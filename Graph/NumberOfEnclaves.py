# Link For Problem: https://leetcode.com/problems/number-of-enclaves/

class Solution:

    def dfs(self, i: int, j: int, grid: list[list[int]]) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return

        grid[i][j] = 0

        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)

    def numEnclaves(self, grid: list[list[int]]) -> int:
        count: int = 0
        ROW, COL = len(grid), len(grid[0])

        for i in range(ROW):
            for j in range(COL):

                if grid[i][j] == 1 and (i == 0 or i == ROW-1 or j == 0 or j == COL-1):
                    self.dfs(i, j, grid)

        for i in range(ROW):
            for j in range(COL):

                if grid[i][j] == 1:
                    count += 1

        return count
