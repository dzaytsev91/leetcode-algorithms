# repeat


class Solution:
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        stack = []
        for index, value in enumerate(T):
            while stack and T[stack[-1]] < value:
                cursor = stack.pop()
                answer[cursor] = index - cursor
            stack.append(index)
        return answer


if __name__ == '__main__':
    solution = Solution()
    resp = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
