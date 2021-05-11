from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        data = {}
        for letter in p:
            if letter in data:
                data[letter] += 1
            else:
                data[letter] = 1

        left = 0
        right = len(p) - 1
        result = []
        search_data = defaultdict(int)
        for index in range(len(p) - 1):
            search_data[s[index]] += 1
        while right < len(s):
            search_data[s[right]] += 1

            if search_data == data:
                result.append(left)

            if search_data.get(s[left]) > 1:
                search_data[s[left]] -= 1
            else:
                del search_data[s[left]]
            left += 1
            right += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams("abab", "ab"))
