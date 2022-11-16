# Link For Problem: https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:

    def longestOnes(self, nums: list[int], k: int) -> int:
        left, ans, zeros = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            if zeros <= k:
                ans = max(ans, right-left+1)

        return ans
