# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### Naive dfs tracking path
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathP = self.dfs(root, p)
        pathQ = self.dfs(root, q)
        common = []
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] == pathQ[i]:
                common.append(pathP[i])
        return common[-1]
            
    def dfs(self, root, target):
        path = []
        stack = [root]
        while stack:
            current = stack.pop()
            while True:
                if not path:
                    path.append(current)
                    break
                elif not path[-1]:
                    path.pop()
                elif current in [path[-1].left, path[-1].right]:
                    path.append(current)
                    break
                else:
                    path.pop()
            if current and current.val == target.val:
                break
            if current:
                stack.extend([current.right, current.left])
        return path   
    
    
### Taking advantages of BST
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l, r = min(p.val, q.val), max(p.val, q.val)
        current = root
        while current:
            if l <= current.val and r >= current.val:
                return current
            if r <= current.val:
                current = current.left
            else:
                current = current.right
