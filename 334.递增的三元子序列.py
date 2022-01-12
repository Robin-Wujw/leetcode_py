#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = float('inf')
        for i in nums:
            if(i<=a):
                a = i 
            elif(i<=b):
                b = i
            else:
                return True 
        return False

# @lc code=end

