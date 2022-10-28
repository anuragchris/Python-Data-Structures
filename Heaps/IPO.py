# Link For Problem: https://leetcode.com/problems/ipo/

import heapq


class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        cap, pro = [], []

        for c, p in zip(capital, profits):
            heapq.heappush(cap, [c, p])

        for i in range(k):

            while cap and cap[0][0] <= w:
                c, p = heapq.heappop(cap)
                heapq.heappush(pro, [-p, c])

            if not pro:
                break

            w += -heapq.heappop(pro)[0]

        return w
