#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left,right,up,down = 0,n-1,0,n-1
        num = 1
        mat = [[0]*n for _ in range(n)]
        while num <= n*n:
            for i in range(left,right+1):
                mat[up][i] = num
                num += 1
            up += 1
            for j in range(up,down+1):
                mat[j][right] = num
                num += 1
            right -= 1
            for k in range(right,left-1,-1):
                mat[down][k] = num 
                num += 1 
            down -= 1
            for l in range(down,up-1,-1):
                mat[l][left] = num 
                num += 1 
            left += 1 
        return mat
# @lc code=end

