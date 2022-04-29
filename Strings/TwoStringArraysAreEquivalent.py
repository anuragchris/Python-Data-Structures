# Link For Problem: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:

    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    def another_solution(self, word1: list[str], word2: list[str]) -> bool:
        s1 = ''
        s2 = ''

        for i in word1:
            s1 += i

        for i in word2:
            s2 += i

        return s1 == s2
