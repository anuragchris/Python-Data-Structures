# Link For Problem: https://leetcode.com/problems/longest-happy-string/

import heapq


class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        map = []

        if a != 0:
            heapq.heappush(map, [-a, 'a'])

        if b != 0:
            heapq.heappush(map, [-b, 'b'])

        if c != 0:
            heapq.heappush(map, [-c, 'c'])

        res = []

        for i in range(a+b+c):
            c, x = heapq.heappop(map)

            if len(res) >= 2:

                if res[-2:] != [x, x]:
                    res.append(x)

                    if c + 1 != 0:
                        heapq.heappush(map, [c+1, x])

                else:

                    if len(map) == 0:
                        break

                    c1, x1 = heapq.heappop(map)
                    res.append(x1)

                    heapq.heappush(map, [c, x])

                    if c1 + 1 != 0:
                        heapq.heappush(map, [c1+1, x1])

            else:
                res.append(x)
                heapq.heappush(map, [c+1, x])

        return ''.join(res)
