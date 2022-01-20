#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
from itertools import count
import queue


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.headIndex = 0 
        self.count = 0
        self.capicity = k 
    def enQueue(self, value: int) -> bool:
        if(self.count == self.capicity):
            return False 
        self.queue[(self.headIndex + self.count)%self.capicity] = value 
        self.count += 1
        return True 

    def deQueue(self) -> bool:
        if(self.count==0):
            return False
        self.headIndex = (self.headIndex + 1 ) % self.capicity
        self.count -= 1 
        return True 

    def Front(self) -> int:
        if(self.count==0):
            return -1 
        return self.queue[self.headIndex]
    def Rear(self) -> int:
        if(self.count==0):
            return -1
        return self.queue[(self.headIndex + self.count -1) % self.capicity]
    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.capicity:
            return True
        else:
            return False 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

