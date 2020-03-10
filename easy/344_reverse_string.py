from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return
        start_index = 0
        end_index = len(s) - 1
        while True:
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1
            if start_index == end_index:
                return
            if start_index > end_index:
                return


if __name__ == '__main__':
    solution = Solution()
    s1 = ["h", "e", "l", "l", "o"]

    solution.reverseString(s1)
    assert s1 == ["o", "l", "l", "e", "h"]
