class StockSpanner:

    def __init__(self):
        self.stack =[]
        self.cur_day = -1

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1]<=price:
            self.stack.pop()
        self.cur_day +=1
        if self.stack:
            last_day = self.stack[-1][0]
        else:
            last_day =-1
        self.stack.append((self.cur_day,price))
        return self.cur_day -last_day
