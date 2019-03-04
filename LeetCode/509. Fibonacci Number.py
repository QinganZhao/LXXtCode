### recursion
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

### iteration
class Solution:
    def fib(self, N: int) -> int:
        left, right = 0, 1
        for _ in range(N):
            left, right = right, left + right
        return left
