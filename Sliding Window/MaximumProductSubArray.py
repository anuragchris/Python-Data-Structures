# Link For Problem: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans, current = nums[0], 1

        for i in nums:
            current *= i
            ans = max(ans, current)

            if current == 0:
                current = 1

        current = 1

        for i in range(len(nums)-1, -1, -1):
            current *= nums[i]
            ans = max(ans, current)

            if current == 0:
                current = 1

        return ans

    def anotherSolution(self, nums: list[int]) -> int:
        res: int = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue

            temp: int = currMax*n

            currMax = max(currMax*n, currMin*n, n)
            currMin = min(temp, currMin*n, n)

            res = max(res, currMax)

        return res
