#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pos=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            visited[x][y]=1

            ans=0
            if x==0 or y==0:
                ans |= 2

            if x==m-1 or y==n-1:
                ans |= 1     
            
            for dx,dy in pos:
                xx,yy=x+dx,y+dy
                if 0<=xx<m and 0<=yy<n and heights[xx][yy]<=heights[x][y] and not visited[xx][yy]:
                    ans |= dfs(xx,yy)
            return ans            

        memo={}
        res=[]
        for i in range(m):
            for j in range(n):
                visited=[[0]*n for _ in range(m)]
                ans = dfs(i,j)
                memo[(i,j)]=ans
                if ans==3:
                    res.append((i,j))                

        return res
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     def bfs(A):
    #         queue, vis = deque(A), set(A)
    #         while queue:
    #             i, j = queue.popleft()
    #             for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
    #                 if 0<=x<m and 0<=y<n and (x, y) not in vis and heights[x][y]>=heights[i][j]:
    #                     queue.append((x, y))
    #                     vis.add((x, y))
    #         return vis

    #     m, n = len(heights), len(heights[0])
    #     A = {(0, j) for j in range(n)} | {(i, 0) for i in range(m)}
    #     B = {(m-1, j) for j in range(n)} | {(i, n-1) for i in range(m)}
    #     return [[i, j] for i, j in bfs(A) & bfs(B)]
# @lc code=end

