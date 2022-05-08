# Link For Problem : https://leetcode.com/problems/132-pattern/

class Solution:

    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        currMin = nums[0]

        for i in nums[1:]:

            while stack and i >= stack[-1][0]:
                stack.pop()

            if stack and i > stack[-1][1]:
                return True

            stack.append([i, currMin])
            currMin = min(currMin, i)

        return False

    def another_solution(self, nums: list[int]) -> bool:
        stack = []
        third = float('-inf')

        for i in nums[::-1]:

            if i < third:
                return True

            while stack and i > stack[-1]:
                third = stack.pop()

            stack.append(i)

        return False
