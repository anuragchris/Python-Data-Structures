# Link For Problem: https://leetcode.com/problems/determine-if-two-strings-are-close/

from typing import Counter


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:

        dict1, dict2 = Counter(word1), Counter(word2)

        keys = dict1.keys() == dict2.keys()

        if not keys:
            return False

        occurence = sorted(dict1.values()) == sorted(dict2.values())

        return keys and occurence
