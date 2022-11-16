# Link For Problem: https://leetcode.com/problems/count-number-of-nice-subarrays/

from collections import deque


class Solution:

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        dq: deque[int] = deque()

        dq.append(-1)

        ans: int = 0

        for i, num in enumerate(nums):
            if num & 1:
                dq.append(i)

            if len(dq) > k+1:
                dq.popleft()

            if len(dq) == k+1:
                ans += dq[1]-dq[0]

        return ans
