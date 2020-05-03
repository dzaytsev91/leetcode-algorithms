from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        for num in range(max_num):
            if num not in nums:
                return num
        return max_num + 1
