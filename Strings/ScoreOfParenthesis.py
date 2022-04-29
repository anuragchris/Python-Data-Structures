# Link For Problem: https://leetcode.com/problems/score-of-parentheses/

class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        depth, res = 0, 0
        prev = '('

        for i in s:

            if i == '(':
                depth += 1

            else:
                depth -= 1

                if prev == '(':
                    res += 1 << depth

            prev = i

        return res
