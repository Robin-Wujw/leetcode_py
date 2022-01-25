#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#
# @lc code=start
class Solution: 
    def numberOfMatches(self, n: int) -> int:
        if(n==1):
            return 0
        half = int(n/2)
        return half + self.numberOfMatches(int(n/2) + n%2)
    
# @lc code=end

