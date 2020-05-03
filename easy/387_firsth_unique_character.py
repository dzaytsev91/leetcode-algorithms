class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = {}
        for letter in s:
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1

        for i in range(len(s)):
            if result[s[i]] == 1:
                return i

        return -1
