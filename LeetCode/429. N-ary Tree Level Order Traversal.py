"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([(root, 0)])
        cache = []
        while queue:
            current, depth = queue.popleft()
            if current:
                cache.append((current.val, depth))
                for child in current.children:
                    queue.append((child, depth+1))
        res = [[] for i in range(cache[-1][1] + 1)]
        for val, depth in cache:
            res[depth].append(val)
        return res
