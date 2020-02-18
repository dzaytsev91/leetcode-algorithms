class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '[', '{']
        match_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for val in s:
            if val in open_brackets:
                stack.append(val)
                continue

            if not stack:
                return False

            if match_brackets[val] != stack.pop():
                return False

        if len(stack) > 0:
            return False

        return True


if __name__ == '__main__':
    assert True is Solution().isValid("([{}])")
    assert False is Solution().isValid("((}))")
    assert False is Solution().isValid("}((}))")
    assert False is Solution().isValid("(())}")
