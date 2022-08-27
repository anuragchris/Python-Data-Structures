# Link For Problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from turtle import left


class Solution:

    def search(self, nums: list[int], target: int) -> bool:
        start, end = 0, len(nums)-1

        while(start <= end):

            while start < end and nums[start] == nums[start+1]:
                start += 1

            while end > start and nums[end] == nums[end-1]:
                end -= 1

            mid: int = start+(end-start)//2

            if nums[mid] == target:
                return True

            else:

                if nums[start] <= nums[mid]:

                    if target >= nums[start] and target <= nums[mid]:
                        end = mid-1
                    else:
                        start = mid+1

                else:

                    if target >= nums[mid] and target <= nums[end]:
                        start = mid+1
                    else:
                        end = mid-1

        return False
