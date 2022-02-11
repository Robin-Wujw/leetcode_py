#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # m , n = len(grid), len(grid[0])
        # vis = [[False]*n for _ in range(m)]

        # def dfs(r,c):
        #     if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:  
        #         return 
        #     vis[r][c] == True 
        #     for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
        #         dfs(x,y)
        
        # for i in range(m):
        #     dfs(i,0)
        #     dfs(i,n-1)
        # for j in range(1,n-1):
        #     dfs(0,j)
        #     dfs(m-1,j)
        # return sum(grid[x][y] and not vis[x][y] for x in range(1,m-1) for y in range(1,n-1))
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:
                return
            vis[r][c] = True
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(x, y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))



# @lc code=end

