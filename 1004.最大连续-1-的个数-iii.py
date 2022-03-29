#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans,sum,left = 0,0,0
        for right in range(len(nums)):
            sum += nums[right] != 1
            while(sum>k):
                sum -= nums[left] != 1
                left += 1 
            ans = max(ans,right-left+1)
        return ans 
# @lc code=end

