#为了快速判断某个坐标是否为障碍物（是否在 obstacles 数组中），我们可以把 obstacles 转成哈希集合，判断坐标是否在哈希集合中。
DIRS =((0,1),(1,0),(0,-1),(-1,0))  #上右下左
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set =set(map(tuple,obstacles))
        ans =x=y =k=0
        for c in commands:
            if c==-1:  #右转
                k=(k+1)%4
            elif c==-2: #左转
                k =(k+3)%4
            else: #直行遇到障碍物停下来
                while c>0 and (x+DIRS[k][0],y+DIRS[k][1]) not in obstacles_set:
                    x+=DIRS[k][0]
                    y+=DIRS[k][1]
                    c -=1
                ans =max(ans,x*x+y*y)
        return ans
