# Link For Problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        result = [i for i in s]
        stack = []

        for i in range(len(result)):

            if result[i] == '(':
                stack.append(i)

            elif result[i] == ')':

                if stack:
                    stack.pop()

                else:
                    result[i] = ''

        if stack:

            for i in stack:
                result[i] = ''

        return ''.join(result)
