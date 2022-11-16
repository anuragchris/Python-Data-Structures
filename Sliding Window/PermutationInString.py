# Link For Problem: https://leetcode.com/problems/permutation-in-string/description/

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        arr1, arr2 = [0]*26, [0]*26

        for i in range(len1):
            arr1[ord(s1[i])-ord('a')] += 1
            arr2[ord(s2[i])-ord('a')] += 1

        for i in range(len2-len1):
            if arr1 == arr2:
                return True

            arr2[ord(s2[i])-ord('a')] -= 1

            arr2[ord(s2[i+len1])-ord('a')] += 1

        return arr1 == arr2
