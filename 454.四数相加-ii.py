#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        Hash = dict()
        for i in nums1:
            for j in nums2:
                sum = i + j 
                if(sum not in Hash):
                    Hash[sum] = 1
                else:
                    Hash[sum] += 1 
        count = 0 
        for i in nums3:
            for j in nums4:
                res = 0 - i - j 
                if(res in Hash):
                    count += Hash[res] 
        return count
# @lc code=end

