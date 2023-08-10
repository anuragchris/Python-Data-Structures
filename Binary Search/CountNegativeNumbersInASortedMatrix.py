# Link For Problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:

    def countNegatives(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])

        if grid[0][0] < 0:
            return row*col

        if grid[row-1][col-1] >= 0:
            return 0

        r, c = row-1, 0
        count: int = 0

        while(r >= 0 and c < col):

            if grid[r][c] < 0:
                r -= 1
                count += col-c
            else:
                c += 1

        return count
