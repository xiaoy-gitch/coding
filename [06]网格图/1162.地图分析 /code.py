class Solution:
    #从所有陆地开始bfs多源搜索，由近距离到远距离进行bfs,最后访问到的海洋，
    #就是距离所有陆地最远的海洋。
    #我们不能从所有海洋n出发多源bfs，因为这样要进行n次bfs,每次记录下距离最先访问到的陆地的距离；然后在所有的这些距离中选出最大的，时间复杂度很高，且距离计算不准确
    def maxDistance(self, grid: List[List[int]]) -> int:
        n =len(grid)
        q =deque()
        #将所有陆地入队
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                     q.append((i,j,0))
        # 检查全陆地或全海洋
        if len(q) == 0 or len(q) == n * n:
            return -1
        ans =0
        while q:
            i,j,dist = q.popleft()
            for x,y in (i,j+1),(i,j-1),(i+1,j),(i-1,j):
                if 0<=x<n and 0<=y<n and grid[x][y]==0:
                    grid[x][y]=1
                    ans =dist+1
                    q.append((x,y,dist+1))
        return ans                    
