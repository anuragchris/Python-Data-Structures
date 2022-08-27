# Link For Problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from heapq import heappop, heappush


class Solution:

    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = []

        temp: int = min(len(nums1), k)

        for i in range(temp):
            heappush(heap, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))

        ans = []

        while k > 0 and heap:
            _, n1, n2, idx = heappop(heap)

            ans.append([n1, n2])

            if idx+1 < len(nums2):
                heappush(heap, (n1 + nums2[idx+1], n1, nums2[idx+1], idx+1))

            k -= 1

        return ans
