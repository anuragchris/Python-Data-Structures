# Link For Problem: https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:

    def maxTurbulenceSize(self, arr: list[int]) -> int:
        left, right = 0, 1
        ans, prev = 1, ""

        while right < len(arr):

            if arr[right-1] > arr[right] and prev != ">":
                ans = max(ans, right-left+1)
                right += 1
                prev = ">"

            elif arr[right-1] < arr[right] and prev != "<":
                ans = max(ans, right-left+1)
                right += 1
                prev = "<"

            else:
                right = right+1 if arr[right] == arr[right-1] else right
                left = right-1
                prev = ""

        return ans
