# Link For Problem: https://leetcode.com/problems/custom-sort-string/

import collections


class Solution:

    def customSortString(self, order: str, s: str) -> str:
        map = {}

        for i in range(len(order)):
            map[order[i]] = i

        return ''.join(sorted(s, key=lambda t: map.get(t, -1)))

    def another_solution(self, order: str, s: str) -> str:
        counter = collections.Counter(s)

        res = []

        for i in order:

            if i in counter:
                res.extend([i]*counter[i])
                counter.pop(i)

        for k, v in counter.items():
            res.extend(k*v)

        return ''.join(res)


sol = Solution()
print(sol.another_solution("cba", "abcd"))
