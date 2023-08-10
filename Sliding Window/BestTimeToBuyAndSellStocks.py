# Link For Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = sys.maxsize, 0

        for i in prices:
            buy = min(buy, i)
            sell = max(sell, i-buy)

        return sell
