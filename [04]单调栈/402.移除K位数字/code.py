class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        #从左向右遍历，先将左边的大元素删除
        for digit in num:
            while k and stack and digit<stack[-1]:
                stack.pop()
                k-=1
            stack.append(digit)
        if k:    #已经是单调递增的了，右边的元素大，可以直接去掉
            ans = stack[:-k]
        else:
            ans = stack
        return ''.join(ans).lstrip('0') or "0"  
        #如果前面的结果是空字符串 ""，Python 会把它当成 False，于是返回后面的 "0"
