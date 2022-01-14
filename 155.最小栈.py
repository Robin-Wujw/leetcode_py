#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
import queue
from typing import Deque


class MinStack:

    def __init__(self):
        self.queue_in = Deque()
        self.queue_out = Deque()

    def push(self, val: int) -> None:
        self.queue_in.append(val)

    def pop(self) -> None:
        if(len(self.queue_in)==0):
            return None
        else:
            self.queue_in.pop()

    def top(self) -> int:
        if(len(self.queue_in)==0):
            return None 
        else:
            return self.queue_in[-1]

    def getMin(self) -> int:
        min = float('inf')
        for i in self.queue_in:
            if(i < min ):
                min = i
        return min 



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

