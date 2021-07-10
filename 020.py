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
    def isValid(self, s):
        su = Stack()
        for x in s:
            if (x == "("):
                su.push(")")
            elif (x == "["):
                su.push("]")
            elif (x == "{"):
                su.push("}")
            elif((not su.isEmpty()) and su.gettop()==x):
                su.pop()  
            else:
                return False  
        return su.isEmpty() 
if __name__ == "__main__":
    a = Solution()
    s = "("   
    print(a.isValid(s))
