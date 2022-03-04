#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start
from cmath import inf



class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans , n = 0,len(nums)
        for i in range(n):
            MinN,MaxN = inf,-inf
            for j in range(i,n):
                MinN = min(MinN,nums[j])
                MaxN = max(MaxN,nums[j])
                ans += MaxN-MinN
        return ans 

# @lc code=end

