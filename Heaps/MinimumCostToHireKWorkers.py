# Link For Problem: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/

from fractions import Fraction
import heapq


class Solution:

    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:

        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')

        pq = []
        sum = 0

        for ratio, q, w in workers:
            heapq.heappush(pq, -q)
            sum += q

            if len(pq) > k:
                sum += heapq.heappop(pq)

            if len(pq) == k:
                ans = min(ans, ratio*sum)

        return float(ans)
