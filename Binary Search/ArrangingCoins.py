# Link For Problem: https://leetcode.com/problems/arranging-coins/

class Solution:

    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n

        while(start <= end):
            k: int = start+(end-start)//2

            current: int = k*(k+1)//2

            if current == n:
                return k

            if(n > current):
                start = k+1
            else:
                end = k-1

        return end
