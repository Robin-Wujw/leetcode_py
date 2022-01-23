#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#

# @lc code=start
from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.price = SortedList()
        self.timeStamp = {} 
        self.maxTimeStamp = 0
    def update(self, timestamp: int, price: int) -> None:
        if(timestamp in self.timeStamp):
            self.price.discard(self.timeStamp[timestamp])
        self.price.add(price)
        self.timeStamp[timestamp] = price
        if(timestamp>self.maxTimeStamp):
            self.maxTimeStamp = timestamp
    def current(self) -> int:
        return self.timeStamp[self.maxTimeStamp] 

    def maximum(self) -> int:
        return self.price[-1] 

    def minimum(self) -> int:
        return self.price[0] 


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

