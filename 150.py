class Solution:
    def evalRPN(self, tokens):
        """
        根据 逆波兰表示法，求表达式的值。
        有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
        说明：
        整数除法只保留整数部分。
        给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
        输入：tokens = ["4","13","5","/","+"]
        输出：6
        解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
        """
        stack = []
        for item in tokens:
            if(item not in ("+","-","*","/")):
                stack.append(item)
            else:
                first_num,second_num = stack.pop(),stack.pop()
                stack.append(eval(f'{second_num}{item}{first_num}'))
        return int(stack.pop(0))

if __name__ ==  "__main__":
    a = Solution()
    tokens = ["4","13","5","/","+"]
    print(a.evalRPN(tokens))