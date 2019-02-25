class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        opt = [0, 0, 0]
        for cost in costs:
            opt = [cost[i] + min(opt[:i] + opt[i+1:]) for i in range(3)]
        return min(opt)
