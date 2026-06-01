class StockSpanner:

    def __init__(self):
        self.stack =[]  #(价格，跨度)

    #这个函数表示到来一个元素，返回小于等于它的连续元素个数
    def next(self, price: int) -> int:
        span =1   #表示当前元素的个数
        while self.stack and price>=self.stack[-1][0]:
            span+=self.stack.pop()[1]
        self.stack.append((price,span))
        return span
#stack[-1]:表示栈顶元素
