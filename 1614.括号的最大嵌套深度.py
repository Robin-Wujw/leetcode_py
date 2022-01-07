#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        maxL = 0 
        len  = 0 
        for i in s:
            if(i=="("):
                len += 1
            elif(i==")"):
                len -= 1
            maxL = max(len,maxL)
        return maxL

# @lc code=end

