# Link For Problem: https: // leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        map = {}

        for i in nums2:

            while stack and stack[-1] < i:
                map[stack.pop()] = i

            stack.append(i)

        while stack:
            map[stack.pop()] = -1

        for i in range(len(nums1)):
            nums1[i] = map[nums1[i]]

        return nums1
