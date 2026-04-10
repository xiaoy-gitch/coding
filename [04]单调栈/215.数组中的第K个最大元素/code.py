class Solution:
    #快速排序时间复杂度：O(nlogn)
    #快速排序每次都能确定一个元素的最终位置（基准）
    #快速选择排序时间复杂度：O(n)
    #设 N 为数组长度。根据快速排序原理，如果某次哨兵划分后，基准数的索引正好是 N−k ，则意味着它就是第 k 大的数字 。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k  
        def quick(left:int,right:int)->int:
            pivot_index = random.randint(left,right)
            nums[left],nums[pivot_index] = = nums[pivot_index], nums[left]
            pivot = nums[left]
            i, j = left, right
            while i<j:
                while i<j and nums[j]>=pivot:
                    j-=1
                while i<j and nums[i]<=pivot:
                    i+=1
                if i<j:
                    nums[i],nums[j] = nums[j],nums[i]
            nums[left],nums[i] = nums[i],nums[left]
            return i #这就是piovt基准元素所在地 ，是第i+1个最小值
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_pos = partition(left, right)

            if pivot_pos == target:
                return nums[pivot_pos]
            elif pivot_pos < target:
                left = pivot_pos + 1
            else:
                right = pivot_pos - 1

        return -1
