class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        #1.建图
        graph =[[] for _ in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited =[False]*n
        #2.dfs遍历
        def dfs(u):
            visited[u] =True
            count =1
            for v in graph[u]:
                if not visited[v]:
                    count+=dfs(v)
            return count
        ans =total =0
        for i in range(n):
            if not visited[i]:
                count =dfs(i)
                ans +=count*total
                total +=count
        return ans 
