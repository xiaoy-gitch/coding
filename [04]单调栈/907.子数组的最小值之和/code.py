class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-1)
        ans,st =0,[-1]
        for right,x in enumerate(arr):
            while len(st)>1 and arr[st[-1]]>x:
                i =st.pop()
                ans+=arr[i]*(i-st[-1])*(right-i)
            st.append(right)
        return ans%(10**9+7)
