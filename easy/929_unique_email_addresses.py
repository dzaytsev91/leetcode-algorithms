from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = {}
        for email in emails:
            name, host = email.split("@")
            name = name.split("+")[0].replace(".", "")
            cleaned_email = name + "@" + host
            if cleaned_email not in result:
                result[cleaned_email] = 0

        return len(result)
