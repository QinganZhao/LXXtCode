class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i-1<0 or not grid[i-1][j]:
                        res += 1
                    if i+1>=len(grid) or not grid[i+1][j]:
                        res += 1
                    if j-1<0 or not grid[i][j-1]:
                        res += 1
                    if j+1>=len(grid[0]) or not grid[i][j+1]:
                        res += 1
        return res
