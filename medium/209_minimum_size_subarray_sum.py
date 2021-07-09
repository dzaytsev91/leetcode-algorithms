from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = float('inf')
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                result = min(result, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1
        if result == float("inf"):
            return 0
        else:
            return result
