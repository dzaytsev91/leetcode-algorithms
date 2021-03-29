class Solution:
    def helper(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1
        return count

    def countSubstrings(self, s: str) -> int:
        result = 0

        for index in range(len(s)):
            result += self.helper(index, index, s)
            result += self.helper(index, index + 1, s)

        return result
