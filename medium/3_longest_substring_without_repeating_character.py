class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        if not s:
            return 0
        left = 0
        result = 0
        for right in range(len(s)):
            char = s[right]
            if char not in data:
                result = max(result, right-left+1)
            else:
                if data[char] < left:
                    result = max(result, right-left+1)
                else:
                    left = data[char] + 1
            data[char] = right
        return result
