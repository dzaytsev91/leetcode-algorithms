from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        data = {}
        seen = {}
        for num in nums1:
            data[num] = 1

        result = []
        for num in nums2:
            if data.get(num) and not seen.get(num):
                seen[num] = 1
                result.append(num)
        return result
