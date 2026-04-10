class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #从左向右遍历，不断的记录最大值，如果后面有比最大值小的元素，说明这个元素是要参与到排序中的
        #从右向左遍历，不断记录最小值，如果右边有比最小值大的元素，说明这个元素是要参与到排序中的
        n =len(nums)
        min =nums[n-1]
        max =nums[0]
        begin,end =0,-1
        for i in range(n):
            if nums[i]<max:
                end =i
            else:
                max =nums[i]
            if nums[n-i-1]>min:
                begin = n-i-1
            else:
                min =nums[n-i-1]
        return end-begin+1
