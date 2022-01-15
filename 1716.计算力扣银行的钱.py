#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        mon = int(n / 7)
        d   = n % 7
        money = 0 
        for i in range(mon):
            money += (28+i*7)
        for i in range(d):
            money += (mon + 1 + i)
        return money
# @lc code=end

