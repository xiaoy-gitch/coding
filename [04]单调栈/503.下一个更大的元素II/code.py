思想：本题 nums 是一个循环数组，nums[n−1] 右边是 nums[0]。我们可以把 nums 复制一份，拼在 nums 右边，这样就把环形数组变成一般数组了。
例如 [1,2,1] 变成 [1,2,1,1,2,1]。
本题要计算每个元素的下一个更大元素的值（注意是值不是下标），这是单调栈的标准应用。

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans =[-1]*n
        stack =[]
        for i in range(2*n-1,-1,-1):
            while stack and nums[i%n]>=stack[-1]:
                stack.pop()
            if stack and i<n:
                ans[i] = stack[-1]
            stack.append(nums[i%n])
        return ans        
