# Link For Problem: https://leetcode.com/problems/next-greater-element-ii/

from ast import Num
from collections import deque


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = [-1] * len(nums)
        n: int = len(nums)

        dq = deque()

        for i in range(n*2):
            current: int = i % n

            while dq and nums[dq[0]] < nums[current]:
                idx: int = dq.popleft()

                res[idx] = nums[current]

            if i < n:
                dq.appendleft(current)

        return res

    def another_solution(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        res = [-1] * n

        stack: list = []

        for i in range(2*n - 1):
            current: int = nums[i % n]

            while stack and nums[stack[-1]] < current:
                res[stack[-1]] = current
                stack.pop()

            if i < n:
                stack.append(i)

        return res
