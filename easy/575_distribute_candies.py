from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return len(candyType) // 2 if len(candyType) // 2 < len(set(candyType)) else len(set(candyType))
