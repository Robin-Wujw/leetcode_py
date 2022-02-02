#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#

# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1,1]
        while f[-1] < k:
            f.append(f[-1]+f[-2])
        ret,i = 0,len(f) - 1 
        while k:
            if(k>=f[i]):
                k = k-f[i]
                ret += 1
            i -= 1
        return ret  
# @lc code=end

