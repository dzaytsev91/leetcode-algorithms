class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        ans = 0
        for k in d:
            if k + 1 in d:
                ans = max(ans, d[k] + d.get(k + 1))

        return ans
