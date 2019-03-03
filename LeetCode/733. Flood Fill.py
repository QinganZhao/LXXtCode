### recursion
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        self.image = image
        self.dfs(sr, sc, oldColor, newColor)
        return self.image
        
    def dfs(self, r, c, oldColor, newColor):
        if self.image[r][c] == oldColor:
            self.image[r][c] = newColor
            if r - 1 >= 0: 
                self.dfs(r-1, c, oldColor, newColor)
            if r + 1 < len(self.image): 
                self.dfs(r+1, c, oldColor, newColor)
            if c - 1 >= 0:
                self.dfs(r, c-1, oldColor, newColor)
            if c + 1 < len(self.image[0]):
                self.dfs(r, c+1, oldColor, newColor)
            
            
### iteration
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r - 1 >= 0: 
                    stack.append((r-1, c))
                if r + 1 < len(image): 
                    stack.append((r+1, c))
                if c - 1 >= 0:
                    stack.append((r, c-1))
                if c + 1 < len(image[0]):
                    stack.append((r, c+1))
        return image  
