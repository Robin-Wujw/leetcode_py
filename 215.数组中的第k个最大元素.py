#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap,nums[i]) # 使用一个长度为k的最小堆来存运算
        for i in range(k,len(nums)): # 遍历数组之后的元素
            if nums[i] > heap[0]: # 当前元素>堆顶时
                heapq.heappop(heap) # 弹出堆顶
                heapq.heappush(heap,nums[i]) # 当前元素入对
        return heap[0] # 此时的最小堆顶就是数组的第k大元素
# @lc code=end

