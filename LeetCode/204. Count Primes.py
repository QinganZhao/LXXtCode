class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        primeChecker = [True] * n
        if n < 2:
            return 0
        primeChecker[0] = primeChecker[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primeChecker[i]:
                primeChecker[i*i:n:i] = [False] * len(primeChecker[i*i:n:i])
        return sum(primeChecker)
