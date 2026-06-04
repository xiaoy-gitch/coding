class Solution:
    #84 .柱状图的最大矩形面积
    def maxRectangleArea(self,heights:List[int])->int:
        st = [-1] #防止i=0没有左边界
        ans =0
        for right,h in enumerate(heights):
            while len(st)>1 and heights[st[-1]]>=h:
                i = st.pop() #矩形高的下标
                left = st[-1]# 栈顶下面那个数就是 left
                ans = max(ans,heights[i]*(right-left-1))
            st.append(right)
        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n =len(matrix[0])
        heights =[0]*(n+1)# 末尾多一个 0,是为了让栈中所有元素都参与计算
        ans =0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    heights[j]=0
                else:
                    heights[j]+=1
            ans = max(ans,self.maxRectangleArea(heights))
        return ans
