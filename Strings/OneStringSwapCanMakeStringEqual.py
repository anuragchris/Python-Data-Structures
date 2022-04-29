# Link For Problem: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        arr = []

        for chars in zip(s1, s2):

            if chars[0] != chars[1]:
                arr.append((chars[0], chars[1]))

            if len(arr) > 2:
                return False

        if len(arr) == 1 or len(arr) > 2:
            return False

        elif len(arr) == 0:
            return True

        else:

            if arr[0][0] != arr[1][1] or arr[0][1] != arr[1][0]:
                return False

        return True

    def another_solution(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        a, b = -1, -1

        for i in range(len(s1)):
            x, y = s1[i], s2[i]

            if x != y:

                if a == -1:
                    a = i

                elif b == -1:
                    b = i

                else:
                    return False

        if a == -1:
            return True

        elif b == -1:
            return False

        return s1[a] == s2[b] and s1[b] == s2[a]
