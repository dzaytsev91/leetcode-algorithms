from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        for val in groupSizes:
            if val == 0:
                continue
            local_res = []
            for _ in range(val):
                index = groupSizes.index(val)
                local_res.append(index)
                groupSizes[index] = 0

            result.append(local_res)

        return result
