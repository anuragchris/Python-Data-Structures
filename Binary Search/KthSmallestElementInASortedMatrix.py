# Link For Problem: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        length: int = len(matrix)
        low, high = matrix[0][0], matrix[length-1][length-1]

        while(low < high):
            mid: int = low+(high-low)//2
            count: int = self.count(matrix, mid)

            if count < k:
                low = mid+1

            else:
                high = mid

        return low

    def count(self, arr: list[list[int]], target: int) -> int:
        count, length = 0, len(arr)
        i, j = length-1, 0

        while i >= 0 and j < length:

            if arr[i][j] > target:
                i -= 1

            else:
                count = count+i+1
                j += 1

        return count
