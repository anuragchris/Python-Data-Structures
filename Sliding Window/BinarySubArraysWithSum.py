# Link For Problem: https://leetcode.com/problems/binary-subarrays-with-sum/description/

from collections import defaultdict


class Solution:

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        map = defaultdict(int)

        yet, total = 0, 0

        for i in nums:
            yet += i

            if map[yet-goal]:
                total += map[yet-goal]

            if yet == goal:
                total += 1

            map[yet] += 1

        return total
