# Link For Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from tkinter import N


class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        i: int == 1 if len(nums) > 0 else 0

        for n in nums:

            if n > nums[i-1]:
                nums[i] = N
                i += 1

        return i
