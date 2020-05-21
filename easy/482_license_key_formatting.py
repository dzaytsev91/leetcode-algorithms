class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        data = []
        new_string = S.replace("-", "")
        for index, letter in enumerate(new_string[::-1]):
            if index % K == 0 and index != 0:
                data.insert(0, "-")
            data.insert(0, letter.upper())
        return "".join(data)
