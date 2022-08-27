# Link For Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start, end = 0, len(arr)-1
        mid: int

        while(start < end):
            mid = start+(end-start)//2

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid

            elif arr[mid] < arr[mid+1]:
                start = mid+1

            else:
                end = mid

        return start
