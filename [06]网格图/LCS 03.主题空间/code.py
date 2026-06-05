class Solution:
    def largestArea(self, grid: List[str]) -> int:
    
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(x, y, char):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0, True  # 越界 => 接触走廊
            if visited[x][y] or grid[x][y] != char:
                return 0, False
            
            visited[x][y] = True
            area = 1
            touches = False
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # 先检查邻居是否是走廊（包括边界外）
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    touches = True
                elif grid[nx][ny] == '0':
                    touches = True
                else:
                    # 只有在相同字符且未访问时才递归
                    sub_area, sub_touch = dfs(nx, ny, char)
                    area += sub_area
                    touches = touches or sub_touch
            
            return area, touches
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] != '0':
                    area, touches = dfs(i, j, grid[i][j])
                    if not touches:
                        max_area = max(max_area, area)
        return max_area
