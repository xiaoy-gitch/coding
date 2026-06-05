class Solution:
    # 若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数
    # 这道题访问为0的元素，计算池塘的个数，遍历八个方向的
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m,n =len(land),len(land[0])
        ans =[] #往数组中添加元素，在进行排序
        def dfs(i:int,j:int)->int:
            land[i][j]=1# 标记 (x,y) 被访问，避免重复访问
            cnt=1
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if 0<=x<m and 0<=y<n and land[x][y]==0:
                        cnt +=dfs(x,y)
            return cnt
        for i,row in enumerate(land):
            for j,x in enumerate(row):
                if x==0:
                    ans.append(dfs(i,j))
        ans.sort()
        return ans
