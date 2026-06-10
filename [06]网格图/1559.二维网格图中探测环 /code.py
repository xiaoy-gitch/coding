class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int, px: int, py: int) -> bool:
            vis[x][y] = True
            for i, j in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):  # 枚举移动方向
                if ((i != px or j != py) and  # (i, j) 不是上一步的格子 (px, py)
                    0 <= i < m and 0 <= j < n and  # (i, j) 没有出界
                    grid[i][j] == grid[x][y] and  # (i, j) 和 (x, y) 的格子值相同
                    (vis[i][j] or dfs(i, j, x, y))):  # 如果之前访问过 (i, j)，那么找到了环，否则继续递归找
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and dfs(i, j, 0, 0):
                    return True
        return False
