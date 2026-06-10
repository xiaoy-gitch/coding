class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        ans =[]
        m,n =len(grid),len(grid[0])
        l,h =pricing
        x0,y0 =start
        vis ={(x0,y0)}
        q =[(x0,y0)]  #定义为列表便于排序，队列没有sort
        while q:
            #将队列中的元素进行排序，按照2-4规则
            #首先按 grid[p[0]][p[1]]（网格中的值）升序排序
            #如果值相同，则按坐标 p 升序排序（先比行，再比列）
            q.sort(key=lambda p:(grid[p[0]][p[1]],p))
            ans.extend(p for p in q if l <= grid[p[0]][p[1]] <= h)
            if len(ans)>=k:
                return ans[:k]
            #由于q是列表，不是队列，所以不能pop()
            tmp =q
            q =[]
            for i,j in tmp:
                for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
                    if 0<=x<m and 0<=y<n and grid[x][y] and (x,y) not in vis:
                        vis.add((x,y))
                        q.append((x,y))
        return ans
