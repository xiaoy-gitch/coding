最终矩形的最大面积一定是以heights数组中的元素为高的，只需要枚举每个高度heights[i]，不断的向左右两侧扩展宽度，从而找到最大宽度，通过这种方法可以找到所有高度的最大宽度，从而就可以算出最大的矩形面积。
时间复杂度：如果通过暴力的方法，通过两层for循环找到每个高度的最大左右边界，时间复杂度=O(n^2).
有什么方法不用通过两层for循环就能找到左右边界呢？
单调栈！！！
从左向右遍历，如果当前元素比栈顶元素大，就不断的出栈，直到找比当前元素小的索引下标，就这样不断地找到每个高度左边比它小的那一个索引位置left[i];
从右向左遍历，如果当前元素比栈顶元素大，就不断的出栈，直到找比当前元素小的索引下标，就这样不断地找到每个高度右边比它小的那一个索引位置right[i];
这样通过一次for循环就可以找到所有高度的left[i],right[i]。
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n =len(heights)
        ans =0
        left =[-1]*n
        stack1 =[]
        #每个元素都要出栈
        #这里每个元素只入栈一次，出栈一次，所以时间复杂度为O(n)
        for i in range(n):
            while stack1 and heights[stack1[-1]]>=heights[i]:
                stack1.pop()
            if stack1:
                left[i] = stack1[-1]
            stack1.append(i)
        right =[n]*n
        stack2 =[]
        for j in range(n-1,-1,-1):
            while stack2 and heights[stack2[-1]]>=heights[j]:
                stack2.pop()
            if stack2:
                right[j] = stack2[-1]
            stack2.append(j)
        for h,l,r in zip(heights,left,right):
            ans =max(ans,(r-l-1)*h)
        return ans 
