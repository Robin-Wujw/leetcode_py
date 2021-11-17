#
# @lc app=leetcode.cn id=209 lang=python3
#给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum = 0 
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while(sum >= target):
                res = min(j-i+1,res)
                sum -= nums[i]
                i += 1
        return 0 if res==float("inf") else res

# @lc code=end

