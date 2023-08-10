# Link For Problem: https://leetcode.com/problems/degree-of-an-array/

class Solution:

    def findShortestSubArray(self, nums: list[int]) -> int:
        numCount, firstSeen = {}, {}

        degree, minLength = 0, 0

        for i, val in enumerate(nums):
            if val not in firstSeen:
                firstSeen[val] = i

            if val not in numCount:
                numCount[val] = 1
            else:
                numCount[val] += 1

            if numCount[val] > degree:
                degree = numCount[val]
                minLength = i-firstSeen[val]+1

            elif numCount[val] == degree:
                minLength = min(minLength, i-firstSeen[val]+1)

        return minLength
