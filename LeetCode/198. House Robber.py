### naive DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) > 1:
            opt = [nums[0]]
            checker = True
            if nums[1] > nums[0]:
                opt.append(nums[1])
            else:
                opt.append(nums[0])
                checker = False
        for i in range(2, len(nums)):
            if not checker:
                opt.append(opt[i-1] + nums[i])
                checker = True
            elif opt[i-1] < opt[i-2] + nums[i]:
                opt.append(opt[i-2] + nums[i])
                checker = True
            else:
                opt.append(opt[i-1])
                checker = False
        return opt[len(nums)-1]
    
### smart DP
### don't have to use checker, since
### OPT[i-2] + i <> OPT[i-1] has already taken all scenarios into consideration
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, current = 0, 0
        for i in nums:
            prev, current = current, max(prev+i, current)
        return current
