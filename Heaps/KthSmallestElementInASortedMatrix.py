# Link For Problem : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq


class Solution:

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])

                elif matrix[i][j] < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -matrix[i][j])

        return -heapq.heappop(heap)
