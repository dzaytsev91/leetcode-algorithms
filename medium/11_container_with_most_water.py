class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_result = 0
        a_pointer = 0
        b_pointer = len(height)-1
        while a_pointer < b_pointer:
            if height[a_pointer] < height[b_pointer]:
                max_result = max(max_result, height[a_pointer] * (b_pointer - a_pointer))
                a_pointer += 1
            else:
                max_result = max(max_result, height[b_pointer] * (b_pointer - a_pointer))
                b_pointer -= 1
        return max_result


