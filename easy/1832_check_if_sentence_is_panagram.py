class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        data = {}
        for char in sentence:
            if char in data:
                continue
            else:
                data[char] = 1
        return len(data) == 26
