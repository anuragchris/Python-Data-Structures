# Link For Problem: https://leetcode.com/problems/top-k-frequent-elements/

import collections
import heapq


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        if k == len(nums):
            return nums

        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        heap = []
        for key in map:
            heapq.heappush(heap, (-map[key], key))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans

    def another_Solution(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        counter = collections.Counter(nums)

        items = []
        for item in counter.items():
            items.append((-item[1], item[0]))

        heapq.heapify(items)

        return [heapq.heappop(items)[1] for _ in range(k)]
