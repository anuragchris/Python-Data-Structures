# Link For Problem: https://leetcode.com/problems/buddy-strings/


class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            map = [0]*26

            for i in s:
                map[ord(i)-ord('a')] += 1

                if map[ord(i)-ord('a')] > 1:
                    return True

            return False

        first, second = -1, -1

        for i in range(len(s)):

            if(s[i] != goal[i]):
                if first == -1:
                    first = i

                elif second == -1:
                    second = i

                else:
                    return False

        if second == -1:
            return False

        return s[first] == goal[second] and s[second] == goal[first]
