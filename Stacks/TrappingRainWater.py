from tabnanny import check


# Link For Problem : https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maxRight = 0
        maxLeft = 0
        ans = 0

        while(left < right):
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:
                ans += maxLeft-height[left]
                left += 1
            else:
                ans += maxRight-height[right]
                right -= 1

        return ans


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
check = print(Solution().trap(arr))
