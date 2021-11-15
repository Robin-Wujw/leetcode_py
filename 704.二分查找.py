#
# @lc app=leetcode.cn id=704 lang=python3
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2 
            if(target != nums[mid]):
                if(target < nums[mid]):
                    right = mid - 1 
                else:
                    left  = mid + 1
            else:
                return mid 
        return -1
# @lc code=end

