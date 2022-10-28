# Link For Problem: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        ans, left, maxFreq = 0, 0, 0

        for right in range(len(s)):
            count[s[right]] = 1+count.get(s[right], 0)

            maxFreq = max(maxFreq, count[s[right]])

            if (right-left+1)-maxFreq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans
