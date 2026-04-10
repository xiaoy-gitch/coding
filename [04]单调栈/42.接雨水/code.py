class Solution:
    def trap(self, height: List[int]) -> int:
        ans =0
        n =len(height)
        prenum =[0]*n # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        prenum[0] = height[0]
        for i in range(1,n):
            prenum[i] = max(prenum[i-1],height[i])
        sufnum =[0]*n# suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        sufnum[n-1] =height[n-1]  
        for j in range(n-2,-1,-1):
            sufnum[j] = max(sufnum[j+1],height[j])
        for h,pre,suf in zip(height,prenum,sufnum):
            ans +=min(pre,suf)-h
        return ans 
