#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        """
        字符串中可能会包含其他字符 #@￥…… ,踩坑了
        """
        res = ""
        for i in s:
            if ord(i) <= 90 and ord(i) >= 65:
                res += chr(ord(i)|32)
            else:
                res += i
        return res
# @lc code=end

