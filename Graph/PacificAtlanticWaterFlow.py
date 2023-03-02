# Link For Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row: int, col: int, visited: set(), prevHeight: int) -> None:
            if (row, col) in visited or row < 0 or col < 0 or row > ROW-1 or col > COL-1 or heights[row][col] < prevHeight:
                return

            visited.add((row, col))

            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, atl, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])

        ans = []

        for (r, c) in pac:
            if (r, c) in atl:
                ans.append([r, c])

        return ans
