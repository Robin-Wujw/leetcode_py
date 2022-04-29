#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        while(left<right):
            if(left<right and nums[left]%2==0):
                left += 1
            if(left<right and nums[right]%2==1):
                right -= 1 
            nums[left],nums[right] = nums[right],nums[left]
        return nums
# @lc code=end

