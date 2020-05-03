from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        if n == 0:
            return result
        if n == 1:
            return ["1"]
        for num in range(1, n+1):
            if num % 5 == 0:
                if num % 3 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Buzz')
            elif num % 3 == 0:
                if num % 5 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            else:
                result.append(str(num))
        return result
