from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sq = 0
        prev = None
        for index in range(1, len(nums)):
            current = ""
            if nums[index-1] < nums[index]:
                current = "+"
            elif nums[index-1] > nums[index]:
                current = "-"
            if current and current != prev:
                max_sq += 1
                prev = current
        return max_sq+1

