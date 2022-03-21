# Link For Problem : https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while(len(heap) > 1):
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if(first != second):
                heapq.heappush(heap, first-second)

        return 0 if len(heap) == 0 else -heap[-1]
