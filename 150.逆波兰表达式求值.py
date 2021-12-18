#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if(i not in ("+","-","*","/")):
                stack.append(i)
            else:
                first_num,second_num = stack.pop(),stack.pop()
                stack.append(eval(f'{first_num}{i}{second_num}'))
        return int(stack.pop(0))
# @lc code=end

