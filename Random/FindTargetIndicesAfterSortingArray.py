# Link For Problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:

    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        equalTo, lessThan = 0, 0

        for i in nums:

            if i == target:
                equalTo += 1
            elif i < target:
                lessThan += 1

        ans = []

        for i in range(equalTo):
            ans.append(lessThan)
            lessThan += 1

        return ans

    def anotherSolution(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        return ans
