from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        current_chars = defaultdict(int)
        left = 0
        right = 0
        result = 0
        while right < len(s):
            current_chars[s[right]] += 1
            right += 1

            while len(current_chars) > 2:
                current_chars[s[left]] -= 1
                if current_chars[s[left]] == 0:
                    del current_chars[s[left]]
                left += 1
            result = max(result, right-left)
        return result
