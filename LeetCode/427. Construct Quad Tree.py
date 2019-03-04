"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        node = Node(True, False, None, None, None, None)
        if self.checkLeaf(grid) != -1:
            node.isLeaf = True
            node.val = bool(grid[0][0])
        else:
            subs = self.divideGrid(grid)
            node.topLeft = self.construct(subs[0])
            node.topRight = self.construct(subs[1])
            node.bottomLeft = self.construct(subs[2])
            node.bottomRight = self.construct(subs[3])
        return node
    
        
    def checkLeaf(self, grid):
        if sum(map(sum, grid)) == len(grid) * len(grid[0]):
            return 1
        if not sum(map(sum, grid)):
            return 0
        return -1
    
    
    def divideGrid(self, grid):
        mid = len(grid) // 2
        ### first loop j then loop i
        ### row num must remain unchanged first 
        ### or the matrix will be transposed
        topLeft = [[grid[i][j] for j in range(mid)] for i in range(mid)]
        topRight = [[grid[i][j] for j in range(mid, len(grid))] for i in range(mid)]
        bottomLeft = [[grid[i][j] for j in range(mid)] for i in range(mid, len(grid))]
        bottomRight = [[grid[i][j] for j in range(mid, len(grid))] for i in range(mid, len(grid))]
        return (topLeft, topRight, bottomLeft, bottomRight)
