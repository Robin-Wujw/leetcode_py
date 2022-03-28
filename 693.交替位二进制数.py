#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # prev = 2
        # while n:
        #     cur = n % 2
        #     if cur == prev:
        #         return False
        #     prev = cur
        #     n //= 2
        # return True
        res = bin(n)[2:]
        prev = 2
        for i in res:
            if(i != prev):
                prev = i 
            else:
                return False
        return True

# @lc code=end

