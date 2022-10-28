# Link For Problem: https://leetcode.com/problems/reorganize-string/

from collections import Counter
import heapq


class Solution:

    def reorganizeString(self, s: str) -> str:
        map = Counter(s)

        heap = [(-value, key) for key, value in map.items()]

        heapq.heapify(heap)

        ans = []

        while(len(heap) > 1):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            ans.extend([x[1], y[1]])

            if x[0] < -1:
                heapq.heappush(heap, (x[0]+1, x[1]))

            if y[0] < -1:
                heapq.heappush(heap, (y[0]+1, y[1]))

        if heap:
            if heap[0][0] < -1:
                return ""

            ans.append(heap[0][1])

        return "".join(ans)
