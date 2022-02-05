#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        ret  = 0 
        for i in nums:
            if i not in dict:
                dict[i] = 1 
            else:
                dict[i] += 1 
        for i in dict:
            if(dict[i]==1):
                ret += i 
        return ret 

# @lc code=end

