from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        length = len(matrix[0])

        for row in range(length):
            for col in range(row, length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(length):
            matrix[row].reverse()
