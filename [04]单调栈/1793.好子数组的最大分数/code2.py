class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        #从k开始，向两边移动，哪边的值最大就向哪边移动
        n =len(nums)
        min_h=nums[k] #从k开始
        ans =nums[k]
        i =j =k
        for _ in range(n-1):
            if j ==n-1 or (i>0 and nums[i-1]>nums[j+1]):
                i -=1
                min_h =min(min_h,nums[i])
            else:
                j +=1
                min_h =min(min_h,nums[j])
            ans =max(ans ,min_h*(j-i+1))
        return ans 
