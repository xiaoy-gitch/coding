class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #单调栈：从后往前遍历，是为了在处理当前元素时，右边的信息已经准备好，从而用单调栈直接得到答案。
        stack =[]
        n =len(temperatures)
        ans =[0]*n
        for i in range(n-1,-1,-1):  #从后向前遍历是为了先将右侧的值展现出来。
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
                #保持栈是单调递减的
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans 
