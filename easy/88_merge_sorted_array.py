from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for value in nums2:
            nums1[nums1.index(0)] = value

        nums1.sort()
