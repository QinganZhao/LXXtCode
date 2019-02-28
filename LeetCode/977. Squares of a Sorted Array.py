### brutal sort
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, A)))
    
### two pointers
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        pos = 0
        for num in A:
            if num < 0:
                pos += 1
        neg = pos - 1
        while neg >= 0 and pos < len(A):
            if A[neg] ** 2 < A[pos] ** 2:
                res.append(A[neg] ** 2)
                neg -= 1
            else:
                res.append(A[pos] ** 2)
                pos += 1
        while neg >= 0:
            res.append(A[neg] ** 2)
            neg -= 1
        while pos < len(A):
            res.append(A[pos] ** 2)
            pos += 1
        return res
