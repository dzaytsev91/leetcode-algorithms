from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index in range(len(matrix)):
            if matrix[index][-1] >= target:
                for indx in range(len(matrix[index])):
                    if matrix[index][indx] == target:
                        return True
                return False
        return False
