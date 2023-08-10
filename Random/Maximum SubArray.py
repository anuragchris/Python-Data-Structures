# Link For Problem: https://leetcode.com/problems/maximum-subarray/?envType=list&envId=rdtb6ags

class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        ans: int = nums[0]
        current: int = 0

        for n in nums:
            if current < 0:
                current = 0

            current += n
            ans = max(ans, current)

        return ans
