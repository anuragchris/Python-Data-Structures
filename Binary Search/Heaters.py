# Link For Problem: https://leetcode.com/problems/heaters/

import bisect


class Solution:

    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.extend([float('-inf'), float('inf')])
        heaters.sort()

        radius = 0

        i = 1

        for house in houses:

            while heaters[i] < house:
                i += 1

            min_dist = min(house-heaters[i-1], heaters[i]-house)
            radius = max(radius, min_dist)

        return radius

    def another_solution(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()

        heaters = [-float('inf')] + heaters + [float('inf')]
        curr_r = 0

        for i in range(len(houses)):
            l = bisect.bisect_left(heaters, houses[i])

            radius = min(heaters[l] - houses[i], houses[i]-heaters[l-1])
            curr_r = max(curr_r, radius)

        return curr_r
