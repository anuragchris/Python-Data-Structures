# Link For Problem: https://leetcode.com/problems/merge-intervals/solution/

class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        merged: list = []

        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
