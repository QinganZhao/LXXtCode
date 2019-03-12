class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic, maxNums, res = {}, [], len(nums)
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        degree = max(dic.values())
        for num, val in dic.items():
            if val == degree:
                maxNums.append(num)
        for num in maxNums:
            i, j = 0, len(nums)-1
            while nums[i] != num or nums[j] != num:
                if nums[i] != num:
                    i += 1
                if nums[j] != num:
                    j -= 1
            res = min(res, j-i+1)
        return res
