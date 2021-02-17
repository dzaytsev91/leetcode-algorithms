from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start_index = 0
        end_index = len(height) - 1
        while (start_index - end_index) != 0:
            max_area = max(max_area, min(height[start_index], height[end_index]) * (end_index - start_index))
            if height[start_index] < height[end_index]:
                start_index += 1
            else:
                end_index -= 1

        return max_area

