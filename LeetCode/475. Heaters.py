class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses:
            return 0
        houses.sort()
        heaters.sort()
        if heaters[-1] < houses[-1]:
            res = max(heaters[0] - houses[0],
                      houses[-1] - heaters[-1])
        else:
            res = heaters[0] - houses[0]
        for i in range(len(houses)-1, -1, -1):
            while len(heaters) >= 2 and houses[i] < heaters[-2]:
                heaters.pop()
            if len(heaters) <= 1:
                break
            mark = (heaters[-1] + heaters[-2]) / 2
            if houses[i] >= mark:
                res = max(res, heaters[-1] - houses[i])
            else:
                res = max(res, houses[i] - heaters[-2])      
        return res
