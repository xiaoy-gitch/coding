#方法2：
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n =len(grid),len(grid[0])
        if m<3 or n<3 :   #一定没有封闭岛屿
            return 0
        
        def dfs(i:int,j:int)->None:
            nonlocal closed
            if i==0 or i==m-1 or j==0 or j==n-1:
                closed =False   #不是封闭岛屿

            grid[i][j] =1  #防止重复访问
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and grid[x][y] ==0:
                    dfs(x,y)
      
        #从内部开始遍历
        ans =0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] ==0:
                    closed =True
                    dfs(i,j)
                    ans +=closed
        return ans 
