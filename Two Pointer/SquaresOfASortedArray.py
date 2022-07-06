# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:

    def sortedSquares(self, nums: list[int]) -> list[int]:
        if nums[0] >= 0:

            for i, j in enumerate(nums):
                nums[i] = j*j

            return nums

        else:
            i, j = 0, len(nums)-1
            arr = [0 for i in range(len(nums))]
            idx = j

            while i <= j:

                if abs(nums[i]) > abs(nums[j]):
                    arr[idx] = nums[i]*nums[i]
                    i += 1
                    idx -= 1

                else:
                    arr[idx] = nums[j]*nums[j]
                    j -= 1
                    idx -= 1

            return arr
