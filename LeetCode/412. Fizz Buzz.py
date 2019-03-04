class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if not i % 3 or not i % 5:
                word = ''
                if not i % 3:
                    word += 'Fizz'
                if not i % 5:
                    word += 'Buzz'
                res.append(word)
            else:
                res.append(str(i))
        return res
