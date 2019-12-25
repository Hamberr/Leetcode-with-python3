class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        self.row = len(grid)
        self.col = len(grid[0])
        self.have_count = [[0 for i in range(self.col)] for i in range(self.row)]
        res = 0
               
        for i in range(self.row):
            for j in range(self.col):
                cur = self.AreaCur(grid, i, j)
                if cur > res:
                    res = cur     
            
        return res

    def AreaCur(self, grid, r, c):
        #print("zhixing", r, c)
        
        if r >= 0 and r < self.row and c >= 0 and c < self.col and grid[r][c] == 1 and self.have_count[r][c] == 0:
                
            self.have_count[r][c] = 1
            #print(self.have_count)
            #print("havecount", r, c)
            up = self.AreaCur(grid, r - 1, c)
            right = self.AreaCur(grid, r, c + 1)
            down = self.AreaCur(grid, r + 1, c)
            left = self.AreaCur(grid, r, c - 1)
            #print("area", r, ",", c, "=", 1 + up + right + left + down)
            return 1 + up + right + left + down

        else:
            #print("area", r, ",", c, "=", 0)
            return 0
        
