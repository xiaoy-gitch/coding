#方法1：
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n =len(grid),len(grid[0])
        if m<3 or n<3 :   #一定没有封闭岛屿
            return 0
        
        def dfs(i:int,j:int)->None:
            grid[i][j] =1  #防止重复访问
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and grid[x][y] ==0:
                    dfs(x,y)
        #遍历边界
        for i in range(m):
            step =1 if i==0 or i==m-1 else n-1
            for j in range(0,n,step):
                if grid[i][j]==0:
                    dfs(i,j)
        #不从边界开始遍历
        ans =0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] ==0:
                    ans +=1
                    dfs(i,j)
        return ans 
