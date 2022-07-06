# Link For Problem: https://leetcode.com/problems/longest-mountain-in-array/

class Solution:

    def longestMountain(self, arr: list[int]) -> int:
        n: int = len(arr)
        ans, base = 0, 0

        while(base < n):
            end: int = base

            if end+1 < n and arr[end+1] > arr[end]:

                while end+1 < n and arr[end+1] > arr[end]:
                    end += 1

                if end+1 < n and arr[end+1] < arr[end]:

                    while end+1 < n and arr[end+1] < arr[end]:
                        end += 1

                    ans = max(ans, end-base+1)

            base = max(end, base+1)

        return ans
