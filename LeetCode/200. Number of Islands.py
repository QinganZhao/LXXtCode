### dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res, rLim, cLim = 0, len(grid), len(grid[0])
        seen = set()
        for row in range(rLim):
            for col in range(cLim):
                if (row, col) not in seen and grid[row][col] == '1':
                    stack = [(row, col, grid[row][col])]
                    while stack:
                        r, c, isLand = stack.pop()
                        seen.add((r, c))
                        if r-1 >= 0 and (r-1, c) not in seen and grid[r-1][c] == '1':
                            stack.append((r-1, c, grid[r-1][c]))
                        if r+1 < rLim and (r+1, c) not in seen and grid[r+1][c] == '1':
                            stack.append((r+1, c, grid[r+1][c]))
                        if c-1 >= 0 and (r, c-1) not in seen and grid[r][c-1] == '1':
                            stack.append((r, c-1, grid[r][c-1]))
                        if c+1 < cLim and (r, c+1) not in seen and grid[r][c+1] == '1':
                            stack.append((r, c+1, grid[r][c+1]))
                    res += 1
        return res

    
### union find
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if uf.id[uf.genId(r, c)] is not None:
                    if r + 1 < len(grid) and uf.id[uf.genId(r+1, c)] is not None:
                        uf.union(uf.genId(r, c), uf.genId(r+1, c))
                    if c + 1 < len(grid[0]) and uf.id[uf.genId(r, c+1)] is not None:
                        uf.union(uf.genId(r, c), uf.genId(r, c+1))
        return len([uf.id[i] for i in range(len(uf.id)) if uf.id[i] == i])
    
        
class UnionFind:
    def __init__(self, grid):
        self.grid = grid
        self.id = [self.genId(r, c) if grid[r][c] == '1' else None
                   for r in range(len(grid)) for c in range(len(grid[0]))]
        self.size = [1] * len(self.id)
        
    def genId(self, r, c):
        return r * len(self.grid[0]) + c
    
    def union(self, index1, index2):
        root1, root2 = map(self.find, (index1, index2))
        if root1 == root2:
            return
        minor, major = (root1, root2) if self.size[root1] > self.size[root2] else (root2, root1)
        self.id[minor] = self.id[major]
        self.size[minor] = self.size[major]
        self.size[major] += self.size[minor]
        
    def find(self, index):
        while index != self.id[index]:
            index, self.id[index] = self.id[index], self.id[self.id[index]]
        return index
