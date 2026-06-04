class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        #可以将道题看作求矩形的最大面积，且必须包含K下标
        st =[]
        ans =0
        n =len(nums)
        left =[-1]*n  #记录每个数左边的最近的小于它的值
        for i,x in enumerate(nums):
            while st and x<=nums[st[-1]]:
                st.pop()
            if st:
                left[i] =st[-1]
            st.append(i)
        right =[n]*n
        st =[]
        for i in range(n-1,-1,-1):
            x =nums[i]
            while st and x<=nums[st[-1]]:
                st.pop()
            if st:
                right[i] =st[-1]
            st.append(i)
        for h,l,r in zip(nums,left,right):
            if l<k<r:
                ans=max(ans,h*(r-l-1))
        return ans
