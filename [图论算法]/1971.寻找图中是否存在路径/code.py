class Solution:
    #1. 方法1：广度优先搜索
    #2. 方法2：深度优先搜索
    #3. 方法3：并查集
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      #方法1：
        # g = defaultdict(list)   #字典
        # for u,v in edges:
        #     g[u].append(v)
        #     g[v].append(u)
        # visited = set([source])  #不能去掉[]
        # q =deque([source])
        # while q:
        #     node =q.popleft()
        #     if node ==destination:
        #         return True
        #     for p in g[node]:
        #         if p not in visited:
        #             visited.add(p)
        #             q.append(p)
        # return False
      #方法2：
        # g = defaultdict(list)   #字典
        # for u,v in edges:
        #     g[u].append(v)
        #     g[v].append(u)
        # visited = set()
        # def dfs(node):
        #     if node ==destination:
        #         return True
        #     visited.add(node)
        #     for p in g[node]:
        #         if p not in visited and dfs(p):
        #             return True
        #     return False
        # return dfs(source)
      #方法3：
        parent =list(range(n)) #每个顶点的父节点初始化为本结点
        def find(x):
            if parent[x]!=x:
                parent[x] =find(parent[x])
            return parent[x]
        def merge(a,b):
            pa ,pb =find(a),find(b)
            if pa!=pb:
                parent[pa] =pb
        for u,v in edges:
            merge(u,v)
        return find(source)==find(destination)
               
             
                    
