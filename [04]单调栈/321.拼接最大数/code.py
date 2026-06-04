class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums,k):
            st =[]
            delete =len(nums)-k  #k为要保留的个数
            for x in nums:
                while delete and st and st[-1]<x:
                    st.pop()
                    delete -=1
                st.append(x)
            return st[:k]
        def merge(A,B):
            ans =[]
            while A or B:
                bigger =A if A>B else B
                ans.append(bigger.pop(0))
            return ans
        return max(merge(pick_max(nums1,i),pick_max(nums2,k-i)) 
        for i in range(k+1) if i<=len(nums1) and k-i <=len(nums2))
