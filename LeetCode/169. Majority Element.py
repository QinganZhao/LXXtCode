### sorting
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        return sorted(dic.items(), key = lambda x: x[1], reverse = True)[0][0]
    
### divide and conquer    
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums) == 1:
            return nums[0]
        left = self.majorityElement(nums[:len(nums)//2])
        right = self.majorityElement(nums[len(nums)//2:])
        if nums.count(left) > nums.count(right):
            return left
        else:
            return right
