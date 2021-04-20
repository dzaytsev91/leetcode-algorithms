class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        count = 0
        vowels = ("a", "e", "i", "o", "u")
        left = 0
        right = 0
        while right <= len(s)-1:
            if left-1 >=0 and s[left-1] in vowels:
                count -= 1

            if s[right] in vowels:
                count += 1
                max_count = max(max_count, count)

            if (right-left)+1 == k:
                left += 1
                right += 1
            else:
                right += 1

        return max_count
