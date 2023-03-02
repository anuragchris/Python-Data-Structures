# Link For Problem : https://leetcode.com/problems/number-of-islands/

class Solution:

    def dfs(self, grid: list[list[str]], i: int, j: int) -> None:

        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

    def numIslands(self, grid: list[list[str]]) -> int:
        ans: int = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ans += 1

        return ans
