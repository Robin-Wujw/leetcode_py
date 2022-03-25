#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # ans = 0
        # for i in range(5, n + 1, 5):
        #     print(i)
        #     while i % 5 == 0:
        #         i = i//5
        #         ans += 1
        # return ans
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

# @lc code=end

