from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        vals = [val for row in matrix for val in row]
        heapq.heapify(vals)
        for _ in range(k):
            ans = heapq.heappop(vals)
        return ans
