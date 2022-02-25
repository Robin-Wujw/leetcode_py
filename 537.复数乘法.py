#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1 , comp1 = map(int,num1[:-1].split("+"))
        real2 , comp2 = map(int,num2[:-1].split("+"))
        return f'{real1 * real2 - comp1 * comp2}+'f'{real1*comp2 + comp1*real2}i'
# @lc code=end
