#
# @lc app=leetcode.cn id=1518 lang=python3
# 用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
# 请你计算 最多 能喝到多少瓶酒。
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        while(True):
            if(int(numBottles/numExchange)>0):
                ret += int(numBottles/numExchange)
            else:
                break
            numBottles = int(numBottles/numExchange) + numBottles%numExchange
        return ret   
# @lc code=end

