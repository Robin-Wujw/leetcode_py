#
# @lc app=leetcode.cn id=2022 lang=python3
#
# [2022] 将一维数组转变成二维数组
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if len(original) != (m * n):
            return out
        out = [[0 for _ in range(n)] for _ in range(m )]
        for i in range(m):
            for j in range(n):
                out[i][j] = original[(i * n) + j]
        return out
# @lc code=end

