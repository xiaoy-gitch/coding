class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        t=[[i+1,i-1]for i in range(n)]
        t[n-1]=[n-2]
        t[0]=[1]
        t[x-1].append(y-1)
        t[y-1].append(x-1)
        
        res=[0]*n
        for i in range(n-1):
            vis=[False]*n
            vis[i]=True
            dq=deque([(i,0)])
            while dq:
                f,step=dq.popleft()
                for x in t[f]:
                    if not vis[x]:
                        vis[x]=True
                        dq.append((x,step+1))
                        if x>i:
                            res[step]+=2
        return res

