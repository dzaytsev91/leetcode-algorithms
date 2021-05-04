from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        min_sum = float('inf')
        current_sum = 0
        while right < len(nums):
            current_sum += nums[right]
            while current_sum >= target:
                min_sum = min(min_sum, right+1-left)
                current_sum -= nums[left]
                left += 1
            right += 1
        if min_sum != float("inf"):
            return min_sum
        return 0
