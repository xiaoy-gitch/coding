class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n =len(forest),len(forest[0])
        trees=[]
        for i in range(m):
            for j in range(n):
                if forest[i][j]>1:
                    trees.append((forest[i][j],i,j))
        trees.sort()  #默认按照第一个数值排序
        prex,prey =0,0
        ans =0
        for height,curx,cury in trees:
            steps = self.bfs(forest,prex,prey,curx,cury)
            if steps==-1:  #表示不可达，直接返回-1
                return -1
            ans +=steps
            prex,prey =curx,cury
        return ans
    def bfs(self,forest,startx,starty,targetx,targety)->int:
        m,n =len(forest),len(forest[0])
        q =deque()
        steps =0
        q.append((startx,starty))
        vis =set()
        vis.add((startx,starty))
        while q:
            size =len(q)
            for _ in range(size):
                curx,cury =q.popleft()
                if curx==targetx and cury==targety:
                    return steps
                for x,y in (curx+1,cury),(curx-1,cury),(curx,cury+1),(curx,cury-1):
                    if 0<=x<m and 0<=y<n and ((x,y) not in vis) and forest[x][y]!=0:
                        q.append((x,y))
                        vis.add((x,y))
            steps +=1
        return -1
