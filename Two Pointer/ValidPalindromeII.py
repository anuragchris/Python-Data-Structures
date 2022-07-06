# Link For Problem: https://leetcode.com/problems/valid-palindrome-ii/

class Solution:

    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(s: str, i: int, j: int) -> bool:
            while i < j:

                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        i, j = 0, len(s)-1

        while i < j:

            if s[i] != s[j]:
                return check_palindrome(s, i, j-1) or check_palindrome(s, i+1, j)

            i += 1
            j -= 1

        return True
