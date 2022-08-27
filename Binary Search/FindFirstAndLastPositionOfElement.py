# Link For Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:

    def find_first(self, nums: list[int], target: int) -> int:
        temp: int = -1
        start, end = 0, len(nums)-1

        while(start <= end):
            mid: int = start+(end-start)//2

            if nums[mid] < target:
                start = mid+1

            elif nums[mid] > target:
                end = mid-1

            else:
                temp = mid
                end = mid-1

        return temp

    def find_last(self, nums: list[int], target: int) -> int:
        temp: int = -1
        start, end = 0, len(nums)-1

        while(start <= end):
            mid: int = start+(end-start)//2

            if nums[mid] < target:
                start = mid+1

            elif nums[mid] > target:
                end = mid-1

            else:
                temp = mid
                start = mid+1

        return temp

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result: list[int] = []

        result.append(self.find_first(nums, target))
        result.append(self.find_last(nums, target))

        return result

    def another_solution(self, nums, target):

        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1

            while left <= right:
                mid = (left + right) // 2

                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1

            while left <= right:
                mid = (left + right) // 2

                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        left, right = binarySearchLeft(
            nums, target), binarySearchRight(nums, target)

        return (left, right) if left <= right else [-1, -1]
