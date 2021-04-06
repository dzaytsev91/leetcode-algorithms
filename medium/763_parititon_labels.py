from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        data = {}
        for i in range(len(S)):
            if S[i] in data:
                data[S[i]].append(i)
            else:
                data[S[i]] = [i]
        list_data = []
        for key in data:
            list_data.append(data[key])
        res = []
        for row in list_data:
            if not res or res[-1][1] < row[0]:
                res.append([row[0], row[-1]])
            else:
                res[-1][1] = max(res[-1][1], row[-1])
        result = []
        for row in res:
            result.append((row[1]-row[0]) + 1)
        return result
