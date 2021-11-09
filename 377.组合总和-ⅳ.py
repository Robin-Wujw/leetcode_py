#
# @lc app=leetcode.cn id=377 lang=python3
#   给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# #
#
# [377] 组合总和 Ⅳ
#
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #背包问题
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[-1]
# @lc code=end