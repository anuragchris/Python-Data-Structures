# Link For Problem: https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq


class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        maxReach: int = startFuel

        heap = []

        ans, index = 0, 0

        while maxReach < target:

            while index < len(stations) and stations[index][0] <= maxReach:
                heapq.heappush(heap, [-stations[index][1], stations[index][0]])
                index += 1

            if not heap:
                return -1

            maxReach += -heapq.heappop(heap)[0]
            ans += 1

        return ans
