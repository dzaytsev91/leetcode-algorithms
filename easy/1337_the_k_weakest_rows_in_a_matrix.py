from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        response = []
        max_col = len(mat[0]) - 1

        while max_col >= 0:
            max_row = len(mat) - 1
            while max_row >= 0:
                if mat[max_row][max_col] == 1:
                    response.insert(0, max_row)
                    mat[max_row] = [9] * len(mat[0])
                max_row -= 1
            max_col -= 1

        rows = len(mat) - 1
        while rows >= 0:
            if mat[rows][0] == 0:
                response.insert(0, rows)
            rows -= 1
        return response[:k]
