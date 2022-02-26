#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1 
        minN = nums[0]
        for i in range(len(nums)):
            if(nums[i]>minN):
                ans = max(ans,nums[i]-minN)
            minN = min(minN,nums[i])
        return ans 
# @lc code=end

