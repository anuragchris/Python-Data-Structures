# Link For Problem: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        firstWordVal = ''
        for i in firstWord:
            firstWordVal = firstWordVal+str(ord(i)-97)

        firstWordVal = int(firstWordVal)

        secondWordVal = ''
        for i in secondWord:
            secondWordVal = secondWordVal+str(ord(i)-97)

        secondWordVal = int(secondWordVal)

        targetWordVal = ''
        for i in targetWord:
            targetWordVal = targetWordVal+str(ord(i)-97)

        targetWordVal = int(targetWordVal)

        return True if firstWordVal+secondWordVal == targetWordVal else False

    def another_solution(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first, second, target = 0, 0, 0

        for i in firstWord:
            first = (10*first) + (ord(i)-97)

        for i in secondWord:
            second = (10*second) + (ord(i)-97)

        for i in targetWord:
            target = (10*target) + (ord(i)-97)

        return (first+second) == target
