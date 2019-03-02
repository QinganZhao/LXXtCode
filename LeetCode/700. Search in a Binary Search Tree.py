# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### naive DFS
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = [root]
        while stack:
            current = stack.pop()
            if current.val == val:
                return current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return
    
### taking advantage of BST
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return
