class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i, res = 0, 1
        for j in range(1, len(nums)):
            if nums[j] <= nums[j-1]:
                res = max(res, j-i)
                i = j
        res = max(res, j-i+1)
        return res
