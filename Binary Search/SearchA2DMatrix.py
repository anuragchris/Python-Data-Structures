# Link For Problem: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        if row == 0 or col == 0:
            return False

        start, end = 0, (row*col)-1

        while(start <= end):
            mid: int = start+(end-start)//2

            temp: int = matrix[mid//col][mid % col]

            if temp == target:
                return True

            elif target < temp:
                end = mid-1

            else:
                start = mid+1

        return False
