class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        seed = random.randint(1, self.w[-1])
        l, r = 0, len(self.w)-1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
