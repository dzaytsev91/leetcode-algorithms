from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total = 1
        number_of_zeros = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                number_of_zeros += 1
            else:
                total *= nums[index]

        if number_of_zeros == 1:
            result = [total if value == 0 else 0 for value in nums]
        elif number_of_zeros > 1:
            result = [0 for x in nums]
        else:
            for val in nums:
                result.append(total // val)

        return result
