# Link For Problem: https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict = {}
        result = -1

        for i, c in enumerate(s):

            if c in dict:
                result = max(result, i - dict[c] - 1)
            else:
                dict[c] = i

        return result
