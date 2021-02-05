class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        self.candidates = candidates
        self.backtrack([], 0, target)
        return self.res

    def backtrack(self, path, index, target):
        if target < 0:
            return

        if target == 0:
            self.res.append(path)
            return

        for indx in range(index, len(self.candidates)):
            self.backtrack(path + [self.candidates[indx]], indx, target - self.candidates[indx])

