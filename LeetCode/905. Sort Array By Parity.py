### sorting
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
    
### two pass
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if not i % 2] + [i for i in A if i % 2]
