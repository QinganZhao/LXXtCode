class Solution:
    def findMaximumXOR(self, nums: 'List[int]') -> 'int':
        root = Trie()
        for num in nums:
            current = root
            for i in range(31, -1, -1):
                digit = num & 1 << i
                if digit:
                    if not current.one:
                        current.one = Trie()
                    current = current.one
                else:
                    if not current.zero:
                        current.zero = Trie()
                    current = current.zero
        res = 0
        for num in nums:
            current = root
            val = 0
            for i in range(31, -1, -1):
                digit = num & 1 << i
                if current.one and current.zero:
                    if digit:
                        current = current.zero
                    else:
                        current = current.one
                    val += 1 << i
                else:
                    if (current.one and not digit) or (current.zero and digit):
                        val += 1 << i
                    current = current.one or current.zero
            res = max(res, val)
        return res

class Trie:
    def __init__(self):
        self.one = None
        self.zero = None
