from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dicts = []
        for word in strs:
            data = {}
            if not word:
                if word not in dicts:
                    dicts.append(word)
                    result.append([""])
                else:
                    result[dicts.index(word)].append(word)
                continue
            for letter in word:
                if letter in data:
                    data[letter] += 1
                else:
                    data[letter] = 1

            if data in dicts:
                result[dicts.index(data)].append(word)
            else:
                dicts.append(data)
                result.append([word])
        return result
