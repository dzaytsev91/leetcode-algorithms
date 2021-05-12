from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        vocab = {}
        for k, v in enumerate(order):
            vocab[v] = k
        prev = []
        for i in range(len(words)):
            word = [vocab[char] for char in words[i]]
            if word < prev:
                return False
            prev = word
        return True
