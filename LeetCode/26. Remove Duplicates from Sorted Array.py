class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        j = 0
        for i in range(1, len(nums)):
            if (nums[i] != nums[j]):
                j += 1
                nums[j] = nums[i]
        return j + 1
        
