#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # minRow = [min(row) for row in matrix]
        # maxCol = [max(col) for col in zip(*matrix)]
        # ans = []
        # for i, row in enumerate(matrix):
        #     for j, x in enumerate(row):
        #         if x == minRow[i] == maxCol[j]:
        #             ans.append(x)
        # return ans
        ans = []
        for row in matrix:
            for j, x in enumerate(row):
                if max(r[j] for r in matrix) <= x <= min(row):
                    ans.append(x)
        return ans


# @lc code=end

