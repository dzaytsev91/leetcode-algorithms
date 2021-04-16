from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(numbers)):
            wanted_num = target - numbers[index]
            if wanted_num in seen:
                return [seen[wanted_num]+1, index+1]
            else:
                seen[numbers[index]] = index
