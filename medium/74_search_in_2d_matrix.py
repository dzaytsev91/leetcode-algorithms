from typing import List


class Solution:
    def hasNumber(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return self.hasNumber(row, target)
