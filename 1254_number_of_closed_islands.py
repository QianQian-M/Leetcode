class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        
        
        def dfs(grid,i,j):
            
            if i > len(grid)-1 or j > len(grid[0])-1 or i < 0 or j < 0 or grid[i][j] == 1:
                return
            
            grid[i][j]=1
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
        
        for i in range(len(grid)):
            dfs(grid,i,0)
            dfs(grid,i,len(grid[0])-1)
            
        for j in range(len(grid[0])):
            dfs(grid,0,j)
            dfs(grid,len(grid)-1,j)
        
        count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(grid,row,col)
                    count+=1
        # print(count)        
        # print(grid)
        return count
"""
Before searching, fill out the 0 in the edges
"""