class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        #先将机器的成本按照升序排列
        #筛选出成本高于预算budget的机器
        #只有在容量大于之前机器的容量时再入栈，否则得不偿失，又贵容量又低
        a =[(cost,cap) for cost,cap in zip(costs,capacity) if cost<budget]  #严格小于预算
        a.sort(key =lambda p:p[0])
        stack =[]
        ans =0
        for cost,cap in a:
            while stack and cost+stack[-1][0]>=budget:
                stack.pop()  #弹出当前栈中成本最高的机器
            # 情况1：当前机器单独选
            ans = max(ans, cap)
            
            # 情况2：当前机器 + 栈中机器（如果栈非空）
            if stack:
                ans =max(ans,cap +stack[-1][1])
            if not stack or cap>stack[-1][1]:
                stack.append((cost,cap))
        return ans 
