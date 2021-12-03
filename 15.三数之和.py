#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if(nums[i]>0):
                return result
            if(i>0 and nums[i] == nums[i-1]):
                continue
            left = i + 1 
            right = len(nums) - 1
            while(left<right):
                if(nums[i] + nums[left] + nums[right] > 0):
                    right = right - 1 
                elif(nums[i] + nums[left] + nums[right] < 0):
                    left  = left  + 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left = left + 1
                    right = right - 1 
        return result

# @lc code=end

