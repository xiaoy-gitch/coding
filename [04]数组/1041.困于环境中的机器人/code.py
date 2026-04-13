DRIS =((0,1),(1,0),(0,-1),(-1,0))  #上-右-下-左
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x=y =k =0
        for c in instructions:
            if c=="G":
                x +=DRIS[k][0]
                y +=DRIS[k][1]
            elif c=="R":
                k =(k+1)%4
            else:
                k =(k+3)%4
        return  k!=0 or x==y==0    
