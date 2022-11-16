# Link For Problem: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

import collections


class Solution:

    def longestSubarray(self, nums: list[int], limit: int) -> int:
        ans: int = 0

        minQueue = collections.deque()
        maxQueue = collections.deque()

        left: int = 0

        for right, num in enumerate(nums):

            while minQueue and num < minQueue[-1]:
                minQueue.pop()

            minQueue.append(num)

            while maxQueue and num > maxQueue[-1]:
                maxQueue.pop()

            maxQueue.append(num)

            while maxQueue[0]-minQueue[0] > limit:

                if maxQueue[0] == nums[left]:
                    maxQueue.popleft()

                if minQueue[0] == nums[left]:
                    minQueue.popleft()

                left += 1

            ans = max(ans, right-left+1)

        return ans
