class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        result = 0
        for r in range(len(s)):
            if s[r] not in seen:
                result = max(result, r - left + 1)
            else:
                if seen[s[r]] < left:
                    result = max(result, r - left + 1)
                else:
                    left = seen[s[r]] + 1
            seen[s[r]] = r

        return result
