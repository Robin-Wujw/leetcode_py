#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res, maxLen = 0, 0
        for l, w in rectangles:
            k = min(l, w)
            if k == maxLen:
                res += 1
            elif k > maxLen:
                res = 1
                maxLen = k
        return res


# @lc code=end

