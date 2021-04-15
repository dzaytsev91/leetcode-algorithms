from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return True

            while left < mid and nums[left] == nums[mid]:
                left += 1

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left += 1
                else:
                    right = mid - 1
        return False
