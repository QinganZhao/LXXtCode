class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[-1] + nums[-2] + nums[-3]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return target
        return res
