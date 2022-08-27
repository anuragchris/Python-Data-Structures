# Link For Problem: https://leetcode.com/problems/find-peak-element/

class Solution:

    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        n: int = len(nums)

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return n-1

        start, end = 1, n-2

        while(start <= end):
            mid: int = start+(end-start)//2

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            elif nums[mid-1] > nums[mid]:
                end = mid-1

            else:
                start = mid+1

        return -1
