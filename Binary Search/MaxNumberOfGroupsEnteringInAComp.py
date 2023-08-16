# Link For Problem: https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution:

    def maximumGroups(self, grades: list[int]) -> int:
        n, k = len(grades), 0

        while n >= k+1:
            k += 1
            n -= k

        return k

    def anotherSolution(self, grades: list[int]) -> int:
        n, k = len(grades), 1

        while k*(k+1)//2 <= n:
            k += 1

        return k-1

    def binarySearch(self, grades: list[int]) -> int:
        left, right, n = 0, 1000, len(grades)

        while left < right:
            k: int = (left+right+1)//2

            if k*(k+1)//2 > n:
                right = k-1
            else:
                left = k

        return left
