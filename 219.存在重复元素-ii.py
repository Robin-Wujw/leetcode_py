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
        # 滑动窗口
        # s = set()
        # for i, num in enumerate(nums):
        #     if i > k:
        #         s.remove(nums[i - k - 1])
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False

# @lc code=end

