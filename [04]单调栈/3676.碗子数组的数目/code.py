class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans =0 
        stack =[]
        for i,x in enumerate(nums):
            while stack and nums[stack[-1]]<x:
                j =stack.pop()
                if i-j>1:  #子数组的长度>=3
                    ans+=1
            #左侧的元素大于等于x,此时判断子数组的大小
            if stack and i-stack[-1]>1:
                ans+=1
            stack.append(i)
        return ans 
