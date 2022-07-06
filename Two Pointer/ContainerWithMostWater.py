# Link For Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:

    def maxArea(self, height: list[int]) -> int:
        mx, i, j = 0, 0, len(height)-1

        while i < j:

            if(height[i] < height[j]):
                temp: int = (j-i)*height[i]
                mx = max(mx, temp)
                i += 1

            else:
                temp: int = (j-i)*height[j]
                mx = max(mx, temp)
                j -= 1

        return mx
