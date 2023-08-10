# Link For Problem: https://leetcode.com/problems/time-based-key-value-store/

import collections


class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]

        if not values:
            return ''

        left, right = 0, len(values)-1

        while left+1 < right:
            mid = left+(right-left)//2

            time, value = values[mid]

            if time == timestamp:
                return value

            if time > timestamp:
                right = mid
            else:
                left = mid

        if values[right][0] <= timestamp:
            return values[right][1]

        elif values[left][0] <= timestamp:
            return values[left][1]

        else:
            return ''
