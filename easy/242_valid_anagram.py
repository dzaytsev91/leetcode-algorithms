class Solution:

    def get_letters_count(self, s: str):
        data = {}
        for letter in s:
            if letter not in data:
                data[letter] = 1
            else:
                data[letter] += 1
        return data

    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_letters_count(s) == self.get_letters_count(t)
