#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if(n==0):
            return 1 
        if(n==1):
            return 10
        res,cur = 10,9
        for i in range(n-1):
            cur *= 9-i 
            res += cur 
        return res  

# @lc code=end

