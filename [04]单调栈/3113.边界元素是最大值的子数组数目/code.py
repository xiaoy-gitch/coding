class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        #1.初始化答案
        ans =len(nums)
        #2.在栈中设置哨兵节点，这样就不用判断栈中是否还有元素了
        st=[(inf,0)]  
        for num in nums:
            while num>st[-1][0]:
                st.pop()
            if num == st[-1][0]:
                ans+=st[-1][1]
                st[-1][1] +=1   #表示该元素出现的次数
            else:
                st.append([num,1])
        return ans
