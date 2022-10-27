class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        current_max = 0
        result = 0
        data = {}
        while right < len(s):
            if s[right] not in data:
                data[s[right]] = right
                right += 1
                result = max(result, len(data))
            else:
                del data[s[left]]
                left += 1
        return result
