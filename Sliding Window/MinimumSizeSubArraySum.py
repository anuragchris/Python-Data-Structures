# Link For Problem: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, total = 0, 0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1

        return 0 if res == float('inf') else res
