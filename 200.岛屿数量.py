#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c] = "0" 
        nr,nc = len(grid),len(grid[0])
        for x,y in ([r-1,c],[r+1,c],[r,c-1],[r,c+1]):
            if(0<=x<nr and 0<=y<nc and grid[x][y]=="1"):
                self.dfs(grid,x,y)

    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid),len(grid[0])
        if(r == 0):
            return 0 
        num = 0 
        for x in range(r):
            for y in range(c):
                if(grid[x][y]=="1"):
                    num += 1 
                    self.dfs(grid,x,y)
        return num 
# @lc code=end

