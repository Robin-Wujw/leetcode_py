#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
from typing import Deque
# @lc code=start
class MyQueue:

    def __init__(self):
        self.queue_in = Deque()
        self.queue_out = Deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if(self.empty()):return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.appendleft(self.queue_in.pop())
        self.queue_in,self.queue_out = self.queue_out,self.queue_in
        return self.queue_out.pop()

    def peek(self) -> int:
        if(self.empty()):return None
        return self.queue_in[0]    

    def empty(self) -> bool:
        return len(self.queue_in)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

