# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from math import ceil


class Solution:

    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, int(1e6)

        while left < right:
            mid: int = left+(right-left)//2
            sum: int = 0

            for i in nums:
                sum += ceil(i/mid)

            if sum > threshold:
                left = mid+1
            else:
                right = mid

        return left
