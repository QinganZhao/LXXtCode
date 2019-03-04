### use sum trick
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum, Sum = [], 0
        for num in nums:
            Sum += num
            self.sum.append(Sum)

    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.sum[j]
        return self.sum[j] - self.sum[i-1]
    
    
### pythonic cheating
class NumArray:

    def __init__(self, nums: List[int]):
        self.list = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.list[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
