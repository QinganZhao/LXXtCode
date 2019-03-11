class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic, res = {}, []
        if k < 0:
            return 0
        if k == 0:
            res = 0
            for num in nums:
                dic[num] = dic.get(num, 0) + 1
            for num in dic:
                if dic[num] > 1:
                    res += 1
            return res
        for num in nums:
            if num != dic.get(num-k):
                dic[num-k] = dic.get(num-k, []) + [num]
            if num != dic.get(num+k):
                dic[num+k] = dic.get(num+k, []) + [num]
        for num in nums:
            if num in dic:
                res.extend([num + i for i in dic[num]])
        return len(set(res))
