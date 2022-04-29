# Link For Problem: https://leetcode.com/problems/check-if-a-string-can-break-another-string/


import collections


class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        freq1, freq2 = [0]*26, [0]*26

        for i in s1:
            freq1[ord(i)-97] += 1

        for i in s2:
            freq2[ord(i)-97] += 1

        count1, count2 = 0, 0
        flag1, flag2 = False, False

        for i in range(26):
            count1 += freq1[i]
            count2 += freq2[i]

            if count1 > count2:
                flag1 = True

            elif count2 > count1:
                flag2 = True

            if flag1 and flag2:
                return False

        return True

    def check(self, d1, d2):
        s = 0

        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]

            if s < 0:
                return False

        return True

    def optimized(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)

        return self.check(d1, d2) or self.check(d2, d1)
