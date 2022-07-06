# Link For Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        i: int = 0

        for n in nums:

            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1

        return i
