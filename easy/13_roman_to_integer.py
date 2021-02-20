class Solution:
    data = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        letters = list(s)
        letters.reverse()
        last_val = 0
        for letter in letters:
            val = self.data[letter]
            if val < last_val:
                result -= val
            else:
                result += val
            last_val = val
        return result
