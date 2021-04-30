from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        result = 0

        left_max = height[0]
        right_max = height[-1]

        left = 1
        right = len(height) - 1

        while left <= right:
            if height[left] > left_max:
                left_max = height[left]

            if height[right] > right_max:
                right_max = height[right]

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result

