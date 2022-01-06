#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = list()
        for i in path:
            if(i == ".."):
                if(stack):
                    stack.pop()
            elif(i and i !='.'):
                stack.append(i)
        return '/' + '/'.join(stack)
# @lc code=end

