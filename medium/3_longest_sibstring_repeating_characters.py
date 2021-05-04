class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        max_sub = float('-inf')
        current_sub = {}
        while right < len(s):
            if s[right] in current_sub:
                while s[left] != s[right]:
                    current_sub.pop(s[left])
                    left += 1
                current_sub.pop(s[left])
                left += 1

            current_sub[s[right]] = 1
            right += 1

            max_sub = max(max_sub, len(current_sub))

        return max_sub

