# Link For Problem: https://leetcode.com/problems/max-area-of-island/

class Solution:

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()

        def area(row: int, col: int) -> int:
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or (row, col) in seen:
                return 0

            seen.add((row, col))

            return 1 + area(row+1, col) + area(row-1, col) + area(row, col+1) + area(row, col-1)

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

    def iterativeSolution(self, grid: list[list[int]]) -> int:
        seen = set()
        ans = 0

        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):

                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]

                    seen.add((r0, c0))

                    while stack:
                        r, c = stack.pop()
                        shape += 1

                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):

                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):

                                stack.append((nr, nc))
                                seen.add((nr, nc))

                    ans = max(ans, shape)

        return ans
