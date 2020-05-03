class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for letter in s:
            num = num * 26 + (ord(letter) - ord("A") + 1)
        return num

