#
# @lc app=leetcode.cn id=1765 lang=python3
#
# [1765] 地图中的最高点
#

# @lc code=start
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater),len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        q = deque((i,j) for i,row in enumerate(isWater) for j,water in enumerate(row) if water)#所有水域入队
        while(q):
            i,j = q.popleft()
            for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):   
                if(0<=a<m and 0<=b<n and ans[a][b]==-1):
                    print(a,b,i,j)
                    ans[a][b] = ans[i][j] + 1 
                    q.append((a,b))
        return ans

# @lc code=end

