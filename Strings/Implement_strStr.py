# Link For Problem: https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if(len(haystack)) == 0 or len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):

            if haystack.startswith(needle, i):
                return i

        return -1

    def anotherSolution(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if(len(haystack)) == 0 or len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):

            if haystack[i] == needle[0]:

                if len(needle) <= len(haystack)-i:

                    possible: str = haystack[i:i+len(needle)]

                    if possible == needle:
                        return i

                else:
                    return -1

        return -1
