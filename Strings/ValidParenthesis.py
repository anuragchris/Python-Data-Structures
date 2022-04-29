# Link For Problem: https://leetcode.com/problems/valid-parentheses/

class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) == 1 or (len(s) & 1):
            return False

        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for i in s:

            if i in brackets:
                stack.append(i)

            else:

                if len(stack) and brackets[stack[-1]] == i:
                    stack.pop()

                else:
                    return False

        return stack == []
