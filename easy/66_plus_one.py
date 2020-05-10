from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        for num in range(len(digits)):
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
                continue
            else:
                digits[index] += 1
                return digits

        digits.insert(0, 1)
        return digits
