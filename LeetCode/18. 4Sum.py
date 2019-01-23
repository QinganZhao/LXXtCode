class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ress = []
        nums.sort()
        self.NSum(nums, target, 4, [], ress)
        return ress
    
    def NSum(self, nums, target, N, res, ress):
        if N < 2 or len(nums) < N:
            return
        if N == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ress += [res + [nums[left], nums[right]]]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.NSum(nums[i+1:], target-nums[i], N - 1, res + [nums[i]], ress)
        return    
