class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n =len(grid) ,len(grid[0])
        cur_color =grid[row][col]
        visit =[[False]*n for _ in range(m)]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return True  #边界要进行染色
            if visit[i][j]:
                return False
            if grid[i][j] != cur_color:
                return True   #出现了不连通分量
            visit[i][j] = True
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if  dfs(x,y):
                    grid[i][j] = color
            return False  #表示在一个连通分量里，不需要染色
        dfs(row,col)
        return grid
