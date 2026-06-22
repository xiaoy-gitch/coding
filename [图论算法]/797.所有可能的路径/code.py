class Solution:
    #n=len(graph)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n =len(graph)
        ans =[]
        def dfs(node,path):
            if node ==n-1:
                ans.append(path[:]) #保留副本
                return 
            for p in graph[node]:
                path.append(p)
                dfs(p,path)
                path.pop() #回溯
        dfs(0,[0])
        return ans 
