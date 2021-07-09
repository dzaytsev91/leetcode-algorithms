from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            result = max(result, right - left)
        return result
