from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_word = "".join(sorted(p))
        window_start = 0
        result = []
        word = ""
        for index in range(len(s)):
            word += s[index]
            if len(word) == len(sorted_word):
                sorted_word2 = "".join(sorted(word))
                if sorted_word2 == sorted_word:
                    result.append(window_start)
                window_start += 1
                word = word[1:]
        return result
