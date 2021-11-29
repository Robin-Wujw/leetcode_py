#
# @lc app=leetcode.cn id=349 lang=python3
# 给定两个数组，编写一个函数来计算它们的交集。
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        vocab1 = []
        vocab2 = []
        ret   = []

        for i in nums1:
            if i not in vocab1:
                vocab1.append(i)
        for i in nums2:
            if(i in vocab1 and i not in vocab2):
                vocab2.append(i)
                ret.append(i)
        return ret
# @lc code=end

