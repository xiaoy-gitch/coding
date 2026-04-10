class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#方法1
#暴力
        m,n =len(nums1),len(nums2)
        res =[-1]*m
        for i in range(m):
            j =nums2.index(nums1[i])
            k = j+1
            while k<n and nums2[k]<nums2[j]:
                k+=1
            res[i] = nums2[k] if k<n else -1
        return res
#方法2：
#利用单调栈的方法，提前计算nums2中每个元素的下一个最大元素、
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #哈希表 + 单调栈
        #从左到右遍历，记录nums2中每个元素的下一个更大值
        idx ={x:i for i ,x in enumerate(nums1)}
        ans =[-1]*len(nums1)
        st =[]
        for x in nums2:
            while st and x>st[-1]:
                ans[idx[st.pop()]] =x
            if x in idx:
                st.append(x)  #只需把num1中的元素入栈
        return ans
