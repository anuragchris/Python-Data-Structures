# Link For Problem: https://leetcode.com/problems/valid-anagram/

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxyz')

    def another_solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for i in range(len(s)):

            freq[ord(s[i])-ord('a')] += 1
            freq[ord(t[i])-ord('a')] -= 1

        for i in freq:

            if i != 0:
                return False

        return True
