# repeat

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(self, result, current_string, open_count, close_count,
                  max_count):

        if (len(current_string)) == max_count * 2:
            result.append(current_string)
            return current_string

        if open_count < max_count:
            self.backtrack(result, current_string + "(", open_count + 1,
                           close_count, max_count)

        if close_count < open_count:
            self.backtrack(result, current_string + ")", open_count, close_count + 1, max_count)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(2))
