#
# @lc app=leetcode.cn id=1 lang=python3
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for id,i in enumerate(nums):
            if((target-i) not in dict):
                dict[target-i] = id
            else:
                continue
        for j in range(len(nums)):
            if(nums[j] in dict and j!=dict[nums[j]]):
                return [j,dict[nums[j]]]


# @lc code=end

