#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left,right,up,down = 0,len(matrix[0])-1,0,len(matrix)-1
        ans = []
        while(True):
            for i in range(left,right+1):
                ans.append(matrix[up][i])
            up += 1
            if(up>down): break
            for i in range(up,down+1):
                ans.append(matrix[i][right])
            right -= 1 
            if(left>right): break 
            for i in range(right,left-1,-1):
                ans.append(matrix[down][i])
            down -= 1
            if(up>down): break
            for i in range(down,up-1,-1):
                ans.append(matrix[i][left])
            left += 1 
            if(left>right): break 
        return ans
# @lc code=end

