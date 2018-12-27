# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        res = float('inf')
        if root.left:
            res = min(self.minDepth(root.left), res)
        if root.right:
            res = min(self.minDepth(root.right), res)
        return res + 1       
