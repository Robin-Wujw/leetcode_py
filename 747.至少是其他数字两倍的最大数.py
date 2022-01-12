#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        max = nums[0]
        temp = 0
        maxi = 0 
        for i in range(1,len(nums)):
            if(max < nums[i]): 
                temp = max 
                max = nums[i]
                maxi = i 
            elif(temp < nums[i]):
                temp = nums[i]
        if(temp*2<=max):
            return maxi 
        else:
            return -1

# @lc code=end

