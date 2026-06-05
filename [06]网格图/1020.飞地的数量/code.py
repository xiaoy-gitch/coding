class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visit =[[False]*n for _ in range(m)]
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or visit[i][j] or grid[i][j]==0:
                #超出边界和访问过，单元格是海洋都要直接返回
                return 
            visit[i][j] =True
            for (x,y) in (i,j+1),(i,j-1),(i+1,j),(i-1,j):
                if 0<=x<m and 0<=y<n and not visit[x][y] and grid[x][y]==1:
                    dfs(x,y)
            return 
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(1,n-1):
            dfs(0,j)
            dfs(m-1,j)

        return sum(grid[i][j] and not visit[i][j] for i in range (1,m-1) for j in range (1,n-1))
        #这里不包含边界，因为边界单元格一定可以出边界
