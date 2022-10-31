class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) < 2:
            return True
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[row_index])):
                row_idx = row_index
                col_idx = col_index
                while row_idx < len(matrix) and col_idx < len(matrix[row_idx]):
                    if matrix[row_index][col_index] != matrix[row_idx][col_idx]:
                        return False
                    row_idx += 1
                    col_idx += 1
        return True
