#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n 
        for j in range(n):
            col = j 
            for row in grid:
                dir = row[col]
                col += dir 
                if(col < 0 or col > n or row[col]!=dir):
                    break
            else: #这里是 for跟着的else  表示如果for没有被break 则执行这个
                ans[j] = col 
        return ans 
# @lc code=end

