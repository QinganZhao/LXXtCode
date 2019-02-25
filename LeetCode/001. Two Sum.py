class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Dict = {}
        for i in range(len(nums)):
            Dict[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in Dict and i != Dict[nums[i]]:
                return [i, Dict[nums[i]]]