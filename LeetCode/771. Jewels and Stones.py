class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = collections.defaultdict(int)
        for j in J:
            jewels[j] = 1
        res = 0
        for s in S:
            if jewels.get(s):
                res += 1
        return res
