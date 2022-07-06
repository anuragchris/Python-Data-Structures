# Link For Problem: https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        prod, left, ans = 1, 0, 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right-left+1

        return ans
