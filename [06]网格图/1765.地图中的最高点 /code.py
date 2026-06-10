class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    ans[i][j] = 0 
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for di in dirs:
                    nx, ny = x + di[0], y + di[1]
                    if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                        ans[nx][ny] = h
                        q.append((nx, ny))
            h += 1
        return ans
