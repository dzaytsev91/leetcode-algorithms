from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = float("inf")

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < result:
                result = nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return result
