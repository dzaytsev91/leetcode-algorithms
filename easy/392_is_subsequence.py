class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        index = 0
        for char in t:
            if char == s[index]:
                index += 1
                if len(s) == index:
                    return True
        return False
