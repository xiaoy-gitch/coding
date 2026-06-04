class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #按结束时间排序
        events.sort(key=lambda p:p[1])
        st =[]
        ans =0
        for start_time,end_time,value in events:

            ans = max(ans, value)   #先判断当前活动的最大值
            #二分查找前面有序的列表，找到第一个结束时间小于当前开始时间的活动
            if st:
                i = bisect_left(st,(start_time,))-1  #最后面一个小于开始时间的。
                if i >= 0:
                    ans =max(ans,st[i][1]+value)  #有满足条件的就选择两个活动
            
            if not st or value>st[-1][1]:  #只有后面的活动价值大才入栈
                st.append((end_time,value))
        return ans
