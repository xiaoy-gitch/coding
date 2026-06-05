class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n =len(grid),len(grid[0])
        ans =0
        def dfs(i:int,j:int)->int:
            val = grid[i][j]
            grid[i][j]=0

            for x,y in (i,j+1),(i,j-1),(i-1,j),(i+1,j):
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    val +=dfs(x,y)
            return val
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x:
                    if dfs(i,j)%k==0:
                        ans +=1
        return ans                     
