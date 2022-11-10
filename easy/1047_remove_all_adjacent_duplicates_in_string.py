class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                if char == stack[-1]:
                    stack.pop()
                    continue
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return "".join(stack)
