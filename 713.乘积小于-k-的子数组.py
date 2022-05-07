#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, s, i = 0, 1, 0
        for j,num in enumerate(nums):
            s = s * num
            while(i<=j and s>=k):
                s = s // nums[i]
                i = i + 1 
            ans += j - i + 1 
        return ans 
# @lc code=end

