# Link For Problem : https://leetcode.com/problems/largest-rectangle-in-histogram/

import re


def largestRectangleArea(self, heights: list[int]) -> int:
    if len(heights) == 0:
        return 0

    left = [1]*len(heights)
    right = [1]*len(heights)
    # left.append[-1]

    for i in range(1, len(heights)):
        temp = i-1

        while(temp >= 0 and heights[temp] >= heights[i]):
            temp -= left[temp]

        left[i] = i-temp

    for i in range(len(heights)-2, -1, -1):
        temp = i+1

        while(temp < len(heights) and heights[temp] >= heights[i]):
            temp += right[temp]

        right[i] = temp-i

    ans = 0

    for i in range(len(heights)):
        ans = max(ans, heights[i]*(right[i]+left[i]-1))

    return ans
