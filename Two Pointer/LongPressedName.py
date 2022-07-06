# Link For Problem: https://leetcode.com/problems/long-pressed-name/

class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False

        i, m, n = 0, len(name), len(typed)

        for j in range(len(typed)):

            if i < m and name[i] == typed[j]:
                i += 1

            else:
                if j == 0 or typed[j] != typed[j-1]:
                    return False

        return i == m
