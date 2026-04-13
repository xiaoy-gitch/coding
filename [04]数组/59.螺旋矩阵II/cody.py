DIRS =((0,1),(1,0),(0,-1),(-1,0))  #右-下-左-上
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans =[[0]*n for _ in range(n)]
        i=j=di =0
        for num in range(1,n*n+1):
            ans[i][j] =num
            x,y =i+DIRS[di][0] ,j+DIRS[di][1]
            #越界/元素值存在，则改变方向
            if x<0 or x>=n or y<0 or y>=n or ans[x][y]:
                di =(di+1)%4
            i +=DIRS[di][0]
            j +=DIRS[di][1]
        return ans
