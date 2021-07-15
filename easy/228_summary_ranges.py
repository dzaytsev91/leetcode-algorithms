from typing import List


class Solution:
    def format_seq(self, start, end):
        if start == end:
            return str(end)
        return f"{start}->{end}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        start_group = None
        end_group = None
        result = []

        for num in nums:
            if start_group is None:
                start_group = num
                end_group = num
                continue

            if num - end_group == 1:
                end_group = num
            else:
                result.append(self.format_seq(start_group, end_group))
                start_group = num
                end_group = num

        if start_group is not None and end_group is not None:
            result.append(self.format_seq(start_group, end_group))

        return result

