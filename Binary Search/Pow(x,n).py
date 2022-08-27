# Link For Problem: https://leetcode.com/problems/powx-n/

class Solution:

    def myPow(self, x: float, n: int) -> float:
        ans: float = 1.0
        nn: int = n

        if nn < 0:
            nn *= -1

        while(nn > 0):

            if nn & 1:
                ans *= x
                nn -= 1
            else:
                x *= x
                nn >>= 1

        return 1/ans if n < 0 else ans
