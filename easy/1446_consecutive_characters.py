class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        max_count = 1
        current_count = 1
        current_letter = s[0]
        for index in range(1, len(s)):
            if s[index] == current_letter:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1
                current_letter = s[index]
        return max_count
