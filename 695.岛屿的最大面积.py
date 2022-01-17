#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c] = 0
        maxn = 1 
        nr,nc = len(grid),len(grid[0])
        for x,y in ([r-1,c],[r+1,c],[r,c-1],[r,c+1]):
            if(0<=x<nr and 0<=y<nc and grid[x][y]== 1):
                maxn += self.dfs(grid,x,y)
        return  maxn 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxn = 0 
        nr,nc = len(grid),len(grid[0])
        if(nr == 0):
            return 0 
        for x in range(nr):
            for y in range(nc):
                if(grid[x][y]==1):
                    maxn = max(self.dfs(grid,x,y),maxn)
        return maxn
# @lc code=end

