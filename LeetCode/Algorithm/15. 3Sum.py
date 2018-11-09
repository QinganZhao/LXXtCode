class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        lookup = {}
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        for i in nums:
            if i not in lookup:
                lookup[i] = 0
            lookup[i] += 1
        if len(pos) == 0 or len(neg) == 0:
            if 0 in lookup and lookup[0] >= 3:
                return [[0, 0, 0]]
            else:
                return []
        if 0 in lookup and lookup[0] >= 3:
            res += [[0, 0, 0]]
        if 0 in lookup and lookup[0] >= 1:
            Dict = {}
            for j in set(pos):
                Dict[-j] = j
            for j in set(neg):
                if j in Dict:
                    res += [[Dict[j], 0, j]]                        

        for i in set(pos):
            Set1 = []
            Set2 = []
            Dict = {}
            for j in set(neg):
                Dict[-i-j] = j
            for j in set(neg):
                if j in Dict:
                    if -i-j != j and -i-j < 0 and -i-j not in Set1:
                        res += [[j, -i-j, i]]
                        Set1 += [j]
                    if -i-j == j and lookup[j] >= 2 and j not in Set2:
                        res += [[j, j, i]]
                        Set2 += [j]
                        
                        
        for i in set(neg):
            Set1 = []
            Set2 = []
            Dict = {}
            for j in set(pos):
                Dict[-i-j] = j
            for j in set(pos):
                if j in Dict:
                    if -i-j != j and -i-j > 0 and -i-j not in Set1:
                        res += [[i, j, -i-j]]
                        Set1 += [j]
                    if -i-j == j and lookup[j] >= 2 and j not in Set2:
                        res += [[i, j, j]]
                        Set2 += [j]

        return res
