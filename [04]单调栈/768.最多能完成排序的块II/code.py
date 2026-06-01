class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #划分的快按照原顺序块排序后可以形成递增数组
        #要构成排序快，需要保证每个块中的元素要大于它左边块的最大元素，小于它右边块的最大元素
        #通过单调栈的方法，记录每块中的最大值
        #遇到元素小于栈顶元素，则记录栈顶元素head，将栈中元素出栈，最后将栈顶元素head入栈，相当于
        #此时块的最大元素为head
        #始终保持栈中元素是单调递增的。
        stack =[]
        for num in arr:
            if stack and num<stack[-1]:
                head =stack.pop()  #先取出栈顶元素
                while stack and num<stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        return len(stack)
