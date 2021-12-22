#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        result = []
        for i in nums:
            if i not in map_:
                map_[i] = 1
            else:
                map_[i] += 1
        a = sorted(map_.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(a[i][0])
        return result
# @lc code=end

