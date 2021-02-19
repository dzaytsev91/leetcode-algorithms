class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            if len(A) == len(set(A)):
                return False
            return True

        a_list = list(A)
        b_list = list(B)
        indexes = []
        for index in range(len(a_list)):
            if a_list[index] != b_list[index]:
                indexes.append(index)

        if len(indexes) != 2:
            return False

        if A[indexes[0]] == B[indexes[1]] and A[indexes[1]] == B[indexes[0]]:
            return True

        return False
