#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(v > 0 for row in grid for v in row)
        xz = sum(max(grid[i]) for i in range(len(grid)))
        yz = sum(map(max,zip(*grid)))
        return xy+xz+yz
# @lc code=end

