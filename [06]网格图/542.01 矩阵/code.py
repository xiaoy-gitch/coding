class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m ,n =len(mat),len(mat[0])
        q =deque()
        vis =[[False]*n for _ in range(m)]
        ans =[[0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                    vis[i][j] = True
                    ans[i][j]=0
        step =0
        while q:
            
            for _ in range(len(q)):
                x,y =q.popleft()

                for i,j in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0<=i<m and 0<=j<n and not vis[i][j]:
                        #没有被访问过的都是1
                        q.append((i,j))
                        ans[i][j] =step+1
                        vis[i][j] = True
            step +=1
        return ans
