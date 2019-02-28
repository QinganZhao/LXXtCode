class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicDis = {}
        dicInd = {}
        for i, num in enumerate(nums):
            if num in dicInd:
                dicDis[num] = min(dicDis.get(num, float('inf')), 
                                  i - dicInd[num])
            dicInd[num] = i
        print(dicDis)
        if dicDis:
            return min(map(lambda x: x[1], dicDis.items())) <= k
        return False
