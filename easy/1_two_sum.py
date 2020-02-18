class Solution:

    def twoSum(self, a, t):
        if not a:
            return
        for index, val in enumerate(a):
            search_num = t - val
            if search_num in a and index != a.index(search_num):
                return [index, a.index(search_num)]


if __name__ == '__main__':
    array = [2, 7, 11, 15]
    target = 9
    assert [0, 1], Solution().twoSum(array, target)
