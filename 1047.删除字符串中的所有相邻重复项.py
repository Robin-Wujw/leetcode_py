#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = list()
        for i in s:
            if a and a[-1] == i:
                a.pop()
            else:
                a.append(i)
        return "".join(a)
# @lc code=end

