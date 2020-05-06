from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        data = {}
        for val in nums:
            if val not in data:
                data[val] = 1
            else:
                data[val] += 1
        sorted_data = sorted(data, key=data.get)
        while len(result) < k:
            result.append(sorted_data.pop())
        return result
