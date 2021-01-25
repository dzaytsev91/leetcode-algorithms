from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_length = 0
        count = 0

        for val in rectangles:
            width, height = val
            max_length = max(max_length, min(height, width))

        for value in rectangles:
            width, height = value
            if width == max_length and height > max_length:
                count += 1
            elif height == max_length and width > max_length:
                count += 1

        return count
