def findUnsortedSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    max1 = nums[0]
    min1 = nums[n - 1]
    l, r = 0, 1
    for i in range(n):
        # 从前往后遍历
        if nums[i] < max1:
            l = i
        else:
            max1 = nums[i]
        # 从后往前遍历
        if nums[n - i - 1] > min1:
            r = n - i - 1
        else:
            min1 = nums[n - i - 1]
    return l - r + 1