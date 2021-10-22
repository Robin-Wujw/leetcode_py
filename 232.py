from typing import Deque
class MyQueue:
    """
        请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

        实现 MyQueue 类：

        void push(int x) 将元素 x 推到队列的末尾
        int pop() 从队列的开头移除并返回元素
        int peek() 返回队列开头的元素
        boolean empty() 如果队列为空，返回 true ；否则，返回 false

    """
    def __init__(self):
        self.queue_in = Deque()
        self.queue_out = Deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)    

    def pop(self) -> int:
        if(self.empty):return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.appendleft(self.queue_in.pop())
        self.queue_in,self.queue_out = self.queue_out,self.queue_in
        return self.queue_out.pop()
    def peek(self) -> int:
        if(self.empty()): return None 
        return self.queue_in[0]

    def empty(self) -> bool:
        return len(self.queue_in) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()