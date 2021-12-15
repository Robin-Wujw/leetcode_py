#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
from typing import Deque
# @lc code=start
class MyStack:

    def __init__(self):
        self.queue_in = Deque()
        self.queue_out = Deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if(self.empty()):return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in,self.queue_out = self.queue_out,self.queue_in
        return self.queue_out.pop()

    def top(self) -> int:
        if(self.empty()):
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        if(len(self.queue_in)==0):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

