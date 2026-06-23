class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
 
        if len(connections) < n - 1:
            return -1
        
        edges = [[] for _ in range(n)]
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)
        
        visited = set()

        def dfs(u: int):
            visited.add(u)
            for v in edges[u]:
                if v not in visited:
                    dfs(v)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans - 1
