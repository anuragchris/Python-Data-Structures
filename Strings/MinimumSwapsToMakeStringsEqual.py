# Link For Problem: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution:

    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        if s1 == s2:
            return 0

        xy, yx = 0, 0,

        for a, b in zip(s1, s2):

            if a != b:
                if a == 'x':
                    xy += 1

                else:
                    yx += 1

        if (xy+yx) % 2 != 0:
            return -1

        else:

            if xy % 2 == 0 and yx % 2 == 0:
                return (xy+yx)//2

            else:
                return 2 + (xy//2) + (yx//2)

    def another_solution(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        if s1 == s2:
            return 0

        xy, yx = 0, 0

        for a, b in zip(s1, s2):

            xy += a == 'x' and b == 'y'
            yx += a == 'y' and b == 'x'

        return (xy//2)+(xy % 2)+(yx//2)+(yx % 2) if xy % 2 == yx % 2 else -1
