class Solution:
    #遇到水或者边界，岛屿的周长都会加1
    #也可以使用dfs，遇到i=0,i=m-1,j=0,j=n-1都属于边界情况，周长加1，如果此时相邻有水域则周长再加1.
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans =0
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x:
                    if i==0 or grid[i-1][j]==0:
                        ans+=1
                    if i==m-1 or grid[i+1][j]==0:
                        ans +=1
                    if j==0 or grid[i][j-1]==0:
                        ans +=1
                    if j ==n-1 or grid[i][j+1]==0:
                        ans +=1
        return ans        
