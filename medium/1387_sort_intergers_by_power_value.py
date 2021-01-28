class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = []
        numbers = []
        powers = []

        for val in range(hi - lo + 1):
            numbers.append(lo + val)

        for val in numbers:
            iterations = 0
            while val != 1:
                if val % 2 == 0:
                    val = val // 2
                    iterations += 1

                else:
                    val = 3 * val + 1
                    iterations += 1
            powers.append(iterations)

        for n in numbers:
            power_index = powers.index(min(powers))
            result.append(numbers[power_index])
            powers[power_index] = 1001

        return result[k - 1]
