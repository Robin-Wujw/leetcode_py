#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)
    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()
    def isEmpty(self):
        """
        判断为空
        """
        return len(self.stack)==0
    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        x = Stack()
        for i in s:
            if(i=="("or i=="{"or i=="["):
                x.push(i)
            else:
                if(x.isEmpty()):
                    return False
                if(i==")"):
                    if(x.gettop()=="("):
                        x.pop()
                    else:
                        return False
                if(i=="}"):
                    if(x.gettop()=="{"):
                        x.pop()
                    else:
                        return False
                if(i=="]"):
                    if(x.gettop()=="["):
                        x.pop()
                    else:
                        return False
        return x.isEmpty()
# @lc code=end

