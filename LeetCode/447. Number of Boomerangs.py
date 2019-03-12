class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            dic = {}
            for j in points:
                dic[self.distance(i, j)] = dic.get(self.distance(i, j), 0) + 1
            for val in dic.values():
                res += val * (val - 1)
        return res
        
    def distance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
