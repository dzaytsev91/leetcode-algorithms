class Solution:

    def isPalindrome(self, s: str) -> bool:
        clear = [x.lower() for x in s if x.isalnum()]

        if clear == "":
            return True

        letters = clear[::]
        for letter in clear:
            if letter != letters.pop():
                return False
        return True
