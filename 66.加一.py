#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from dis import dis


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]<9):
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
                if(i==0):
                    digits.insert(0,1)
                    return digits 
                
# @lc code=end

