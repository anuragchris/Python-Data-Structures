# Link For Problem: https://leetcode.com/problems/rotate-array/

class Solution:

    def reverse(self, arr: list[int], i: int, j: int) -> None:
        l, r = i, j

        while l < r:
            temp: int = arr[l]
            arr[l] = arr[r]
            arr[r] = temp

            l += 1
            r -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
