class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 检查起点是否可达
        if grid[0][0] == 1:
            return -1
        m =len(grid)
        q =deque()
        q.append((0,0,1))
        grid[0][0]=1 #访问过
        while q:
            for _ in range(len(q)):
                i,j,step =q.popleft()
                if i==j==m-1:
                    return step
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0<=x<m and 0<=y<m and grid[x][y]==0:
                            grid[x][y]=1
                            q.append((x,y,step+1))
        return -1
