# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ### 1 node -> 0 path, 0 node -> 0 path so 1 will guarantee that min(path) == 0
        self.max = 1
        self.dfs(root)
        ### length = node_num - 1
        return self.max - 1
        
    def dfs(self, root):
        if root:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            self.max = max(self.max, left + right + 1)
            return max(left, right) + 1
        return 0
