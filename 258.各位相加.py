#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            ans = 0
            while(num>0):
                ans += num%10
                num = num//10
            num = ans
        return num
#数学解法
#        return (num - 1) % 9 + 1 if num else 0
# @lc code=end

