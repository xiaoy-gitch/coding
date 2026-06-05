class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m ,n = len(grid),len(grid[0])
        ans =0
        def dfs(i: int,j: int)->int:
            area =1 #当前位置的面积
            grid[i][j]=0 #将当前访问的陆地更改为海洋，为避免重复访问
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    area +=dfs(x,y)
            return area

        for i ,row in enumerate(grid):
            for j,x in enumerate(row):
                if x : #如果是陆地，则从这个位置进行dfs
                    ans = max(ans,dfs(i,j))
        return ans
