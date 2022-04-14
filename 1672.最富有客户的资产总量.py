#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # max = 0 
        # for i in accounts:
        #     if(sum(i)>max):
        #         max = sum(i)
        # return max 
        return max(map(sum, accounts))
# @lc code=end

