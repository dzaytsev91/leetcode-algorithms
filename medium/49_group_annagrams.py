from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for word in strs:
            letters = tuple(sorted(word))
            if letters in data:
                data[letters].append(word)
            else:
                data[letters] = [word]
        return list(data.values())
