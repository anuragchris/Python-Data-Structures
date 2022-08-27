# Link For Problem : https://leetcode.com/problems/sqrtx/

class Solution:

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        start, end = 1, x

        while(start < end):
            mid: int = (int)(start+(end-start)/2)

            if mid <= x/mid and (mid+1) > x/(mid+1):
                return mid

            elif mid > x/mid:
                end = mid

            else:
                start = mid+1

        return start
