# Link For Problem: https://leetcode.com/problems/fruit-into-baskets/description/

from collections import defaultdict


class Solution:

    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) < 2:
            return 1

        map = defaultdict(int)
        left, ans = 0, 0

        for right in range(len(fruits)):
            map[fruits[right]] += 1

            while len(map) > 2:
                map[fruits[left]] -= 1

                if(map[fruits[left]]) == 0:
                    map.pop(fruits[left])

                left += 1

            ans = max(ans, right-left+1)

        return ans
