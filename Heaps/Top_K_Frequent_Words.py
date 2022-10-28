# Link For Problem: https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
import heapq


class Solution:

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)

        heap = []

        for key, value in counts.items():
            heapq.heappush(heap, Word(value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap).word)

        return res[::-1]


class Word:

    freq: int
    word: str

    def __init__(self, freq, word) -> None:
        self.freq = freq
        self.word = word

    def __lt__(self, other) -> bool:
        if(self.freq == other.freq):
            return self.word > other.word

        return self.freq < other.freq

    def __eq__(self, other) -> bool:
        return self.freq == other.freq and self.word == other.word
