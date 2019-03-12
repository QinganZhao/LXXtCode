### brutal force
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i:]) - nums[i]:
                return i
        return -1
    
### prefix sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == Sum - left - num:
                return i
            left += num
        return -1
