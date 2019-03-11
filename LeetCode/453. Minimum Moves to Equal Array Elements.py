### brutal force (TLE)
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max = max(nums)
        while len(nums) * Max != sum(nums):
            for num in nums:
                if num == Max:
                    Max = float('inf')
                    continue
                num += 1
            Max = max(nums)
            
### sorting
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1, -1, -1):
            res += nums[i] - nums[0]
        return res
