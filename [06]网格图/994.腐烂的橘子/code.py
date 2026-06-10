class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs：先将腐烂的橘子全部入队，从中取出一个腐烂的橘子将其上下左右中的新鲜橘子变成腐烂的橘子，直到队列为空。考虑到会出现不会将全部新鲜橘子去不腐烂掉，所以我们统计最开始新鲜橘子的个数，在腐烂时将其个数减去1，如果最终还有新鲜的橘子则返回-1.
        m =len(grid)
        n =len(grid[0])
        fresh =0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh +=1 #新鲜的橘子
                elif grid[i][j]==2:
                    q.append((i,j))#一开始就腐烂的橘子
        count =0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and fresh:
            count +=1 #在遍历当前腐烂橘子的时候分钟+1
            for _ in range(len(q)):
                x, y = q.popleft()              
                # 感染四个方向的新鲜橘子
                for dx, dy in directions:
                    i, j = x + dx, y + dy                  
                    # 检查边界和是否为新鲜橘子
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        # 新鲜橘子变腐烂
                        grid[i][j] = 2
                        fresh -= 1
                        # 新腐烂的橘子加入队列
                        q.append((i, j))
        return -1 if fresh else count
