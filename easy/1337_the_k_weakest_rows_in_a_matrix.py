from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp = []
        for i,m in enumerate(mat):
            cand = (sum(m), i)
            tmp.append(cand)

        tmp.sort()
        return [i[1] for i in tmp]
