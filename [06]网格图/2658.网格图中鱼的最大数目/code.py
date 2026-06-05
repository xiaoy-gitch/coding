class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans =0
        def dfs(i:int,j:int)->int:
            cnt =grid[i][j]
            grid[i][j]=0 #标记访问过
            for x,y in (i,j+1),(i,j-1),(i-1,j),(i+1,j):
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    cnt +=dfs(x,y)
            return cnt

        for i,row in enumerate(grid):
            for j ,x in enumerate(row):
                if x :
                    ans =max(ans,dfs(i,j))
        return ans 
