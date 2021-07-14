from collections import defaultdict
from typing import List


class Solution:

    # helper func to hind greatest common divisor
    def gcd(self, a, b: int):
        while (a != 0 and b != 0) and a != b:
            if a > b:
                a %= b
            else:
                b %= a
        return a if a > b else b

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        data = defaultdict(int)
        for card in deck:
            data[card] += 1

        current_gcd = 0
        for card, count in data.items():
            current_gcd = self.gcd(current_gcd, count)

        return current_gcd > 1
