# Link For Problem: https://leetcode.com/problems/ugly-number-ii/

import heapq


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        h = [1]
        mul = [2, 3, 5]
        seen = set([1])
        res = []

        while len(res) <= n:
            cur = heapq.heappop(h)
            res.append(cur)

            for m in mul:
                if cur * m not in seen:
                    seen.add(cur*m)
                    heapq.heappush(h, cur * m)

        return res[n-1]
