class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def rec(res, data):
            if not data:
                return

            for index in range(len(data)):
                tmp = res[::]
                tmp.append(data[index])
                tmp.sort()

                if tmp not in result:
                    result.append(tmp)
                    rec(tmp, data[:index] + data[index + 1:])

        rec([], nums)

        return result
