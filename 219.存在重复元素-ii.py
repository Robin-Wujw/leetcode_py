#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        dk = 0
        for i in range(len(nums)):
            if(nums[i] in dict):
                dk = i - dict[nums[i]] 
                if(dk <= k ):
                    print(dict)
                    return True
            dict[nums[i]] = i 
        return False
# @lc code=end

