from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        result = []
        for num in nums1:
            if not nums2:
                return result
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result
