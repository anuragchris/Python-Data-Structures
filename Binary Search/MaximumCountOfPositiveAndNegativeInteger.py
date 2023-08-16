# Link For Problem: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:

    def maximumCount(self, nums: list[int]) -> int:
        n: int = len(nums)
        low, high = 0, n-1
        firstPositive, lastNegative = -1, -1

        if nums[0] == 0 and nums[n-1] == 0:
            return 0

        while low <= high:
            mid = low+(high-low)//2

            if nums[mid] < 0:
                lastNegative = mid
                low = mid+1
            else:
                high = mid-1

        low, high = 0, n-1

        while low <= high:
            mid = low+(high-low)//2

            if nums[mid] > 0:
                firstPositive = mid
                high = mid-1
            else:
                low = mid+1

        if firstPositive == -1 and lastNegative == -1:
            return 0

        if lastNegative == -1:
            return n-firstPositive

        if firstPositive == -1:
            return lastNegative+1

        return max(n-firstPositive, lastNegative+1)
