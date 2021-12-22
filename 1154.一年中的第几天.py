#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        dt = date.split('-')
        a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(dt[0]) != 1900 and int(dt[0]) % 4 ==0:
            a[2] += 1
        return sum(a[: int(dt[1])]) + int(dt[-1])
# @lc code=end

