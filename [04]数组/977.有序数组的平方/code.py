#思想：数组两端的元素的平方最大，所以可以采用双指针的方法，
#对比双指针元素绝对值的最大值，依次将最大值的平方放到ans数组中。
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans =[0]*len(nums)
        n =len(nums)
        left,right =0,n-1
        j =n-1
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                ans[j] =nums[left]*nums[left]
                left+=1
            else:
                ans[j] =nums[right]*nums[right]
                right-=1
            j-=1
        return ans
