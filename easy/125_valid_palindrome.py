class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                letters.append(letter.lower())

        left, right = 0, len(letters) - 1
        while left < right:
            if letters[left] != letters[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
