# Link For Problem: https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution:

    def maximumTastiness(self, price: list[int], k: int) -> int:
        price.sort()

        n: int = len(price)
        left, right, ans = 0, price[-1]-price[0], 0

        def check(x: int, price: list[int], k: int) -> bool:
            j, len = 0, 1

            for i in range(1, n):
                if price[i]-price[j] >= x:
                    len += 1
                    j = i

            return True if len >= k else False

        while left <= right:
            mid: int = left+(right-left)//2

            if check(mid, price, k):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans
