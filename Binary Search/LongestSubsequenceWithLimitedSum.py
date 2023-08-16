# Link For Problem: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
import bisect


class Solution:

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        ans = []

        for query in queries:
            idx = bisect.bisect_right(nums, query)
            ans.append(idx)

        return ans
