from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count_data = {}
        groups_count = {}
        for num in nums:
            if num in count_data:
                count_data[num] += 1
            else:
                count_data[num] = 1

        for key in count_data:
            if count_data[key] in groups_count:
                groups_count[count_data[key]].append(key)
            else:
                groups_count[count_data[key]] = [key]

        for item in sorted(groups_count, reverse=True):
            result.extend(groups_count[item])
        return result[:k]
