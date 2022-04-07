#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return len(s) == len(goal) and goal in s + s
        m, n = len(s) , len(goal)
        if(m != n):
            return False
        for i in range(n):
            for j in range(n):
                if(s[(i+j)%n]!=goal[j]):
                    break
            else:
                return True
        return False

# @lc code=end

