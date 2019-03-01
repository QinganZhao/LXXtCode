# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        node = root
        if node.left or node.right:
            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)
        return root
