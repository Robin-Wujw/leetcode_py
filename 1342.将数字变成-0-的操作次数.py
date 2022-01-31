#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # count = 0
        # while num!=0:
        #     if(num % 2 == 0):
        #         num = num / 2 
        #         count += 1 
        #         continue 
        #     else:
        #         num = num - 1
        #         count += 1 
        #         continue
        # return count
        ans = 0
        while num:
            ans += num & 1
            if num > 1:
                ans += 1
            num >>= 1
        return ans
# @lc code=end

