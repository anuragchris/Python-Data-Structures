# Link For Problem : https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        for i in range(0, len(nums)-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
