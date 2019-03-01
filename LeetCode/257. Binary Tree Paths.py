# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### path outside the stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path, pathsNode, paths = [], [], []
        stack = [root]
        current = root
        while stack:
            current = stack.pop()
            while True:
                if not path or current in [path[-1].left,
                                           path[-1].right]:
                    path.append(current)
                    break
                else:
                    path.pop()
            if not current.left and not current.right:
                pathsNode.append(path[:])
            elif current.left and current.right:
                stack.extend([current.right, current.left])
            else:
                stack.append(current.left or current.right)
        for pathNode in pathsNode:
            paths.append('->'.join(map(lambda x: str(x.val), pathNode)))
        return paths
    
    
### path inside the stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, str(root.val))]
        paths = []
        while stack:
            current = stack.pop()
            if not current[0].left and not current[0].right:
                paths.append(current[1])
            if current[0].right:
                stack.append((current[0].right, current[1] + '->' 
                              + str(current[0].right.val)))
            if current[0].left:
                stack.append((current[0].left, current[1] + '->' 
                              + str(current[0].left.val)))
        return paths
