from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data = {}
        for val in arr:
            if val in data:
                data[val] += 1
            else:
                data[val] = 1

        already_seen = set()
        for key in data:
            if data[key] not in already_seen:
                already_seen.add(data[key])
            else:
                return False
        return True
