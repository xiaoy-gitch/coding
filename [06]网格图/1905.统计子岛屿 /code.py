class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m,n =len(grid2),len(grid2[0])
        def dfs(i,j):
            nonlocal ok
            grid2[i][j] =0
            if grid1[i][j] ==0:
                ok =False
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and grid2[x][y] ==1:
                    dfs(x,y)
        ans =0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    ok =True
                    dfs(i,j)
                    ans +=ok
        return ans
