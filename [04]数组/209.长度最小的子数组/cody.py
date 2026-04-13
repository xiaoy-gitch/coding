# 方法1：前缀和+二分查找
# 由于数组元素都是正值，所以前缀和是递增的，有序的数组可以使用二分查找！
# 方法2：滑动窗口
# 由于是求连续数组的和，所以可以使用滑动窗口来做
#方法1：
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n =len(nums)
        prefix =[0]*(n+1) #prefix[i]=前i个元素的和
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]
        ans =inf
        for i in range(n):
            need = target+prefix[i]
            j =bisect.bisect_left(prefix, need) #找到第一个大于等于need的元素
            if j<=n:
                ans =min(ans,j-i)
        return ans if ans!=inf else 0          
#方法2：
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        ans =inf
        sum=0
        for right,num in enumerate(nums):
            sum+=num
            while sum>=target:
                sum -=nums[left]
                ans =min(ans,right-left+1)
                left+=1
        return ans if ans!=inf else 0
