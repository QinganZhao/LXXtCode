class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            return A
        res = [None] * len(A)
        even = 0
        odd = 1
        while A:
            if A[-1] % 2:
                res[odd] = A.pop()
                odd += 2
            else:
                res[even] = A.pop()
                even += 2
        return res
