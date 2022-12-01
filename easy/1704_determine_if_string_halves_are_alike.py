# Intuition
# Split word to 2 parts and use hash map

# Approach
# Split word into 2 parts, iterate over each part and count number of vowels

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(1)

# Code
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {
            "a": True,
            "e": True,
            "i": True,
            "o": True,
            "u": True,
            "A": True,
            "E": True,
            "I": True,
            "O": True,
            "U": True,
        }
        a_letters_count = 0
        b_letters_count = 0
        a_letters = []
        b_letters = []
        mid_length = len(s)//2
        for index in range(len(s)):
            if index < mid_length:
                a_letters.append(s[index])
            else:
                b_letters.append(s[index])

        for index in range(mid_length):
            a_letter = a_letters[index]
            b_letter = b_letters[index]
            if vowels.get(a_letter):
                a_letters_count += 1
                
            if vowels.get(b_letter):
                b_letters_count += 1

        return a_letters_count == b_letters_count
