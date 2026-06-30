class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        #先将所有的入度初始化为0
        in_degress = [0 for _ in range(numCourses)]
        adj =[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            adj[j].append(i)
            in_degress[i] +=1
        ans =[]
        q =[]
        #将入度为0的节点先入队
        for i in range(len(in_degress)):
            if in_degress[i]==0:
                q.append(i)
        while q:
            top =q.pop(0)
            ans.append(top)
            for j in adj[top]:
                in_degress[j] -=1
                if in_degress[j]==0:
                    q.append(j)
        if len(ans)!=numCourses:
            return []  #说明有环
        return ans
