from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for index in range(len(strs)):
            sorted_word = "".join(sorted(strs[index]))
            if sorted_word not in data:
                data[sorted_word] = [strs[index]]
            else:
                data[sorted_word].append(strs[index])

        result = []
        for key in data:
            result.append(data[key])
        return result

