# Link For Problem: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        arr: list[int] = [0]*3

        count, i, n = 0, 0, len(s)

        for j, char in enumerate(s):
            arr[ord(char)-ord('a')] += 1

            while(arr[0] > 0 and arr[1] > 0 and arr[2] > 0):
                count += n-j
                arr[ord(s[i])-ord('a')] -= 1
                i += 1

        return count
