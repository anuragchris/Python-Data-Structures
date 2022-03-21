# Link For Problem: https://leetcode.com/problems/k-closest-points-to-origin/

import heapq


class Solution:

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        points.sort(key=lambda point: (point[0]**2 + point[1]**2))

        return points[:k]

    def kClosestUsingHeap(self, points: list[list[int]], k: int) -> list[list[int]]:

        distances = []

        for x, y in points:
            dist: int = x**2+y**2

            heapq.heappush(distances, (dist, [x, y]))

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(distances)[1])

        return ans

    def kClosest_Using_nSmallest(self, points: list[list[int]], k: int) -> list[list[int]]:

        k_closest = heapq.nsmallest(k,
                                    points, key=lambda point: point[0]**2+point[1]**2)

        return k_closest
