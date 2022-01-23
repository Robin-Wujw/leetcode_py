#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
from  collections import deque
from dis import dis 


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        dist = [[0]*n for _ in range(m)]
        zero_pos = [(i,j) for i in range(m) for j in range(n) if matrix[i][j]==0]

        q = deque(zero_pos)
        seen = set(zero_pos)

        while q:
            i , j = q.popleft()
            for ni,nj in ([i-1,j],[i+1,j],[i,j-1],[i,j+1]):
                if(0<=ni<m and 0<=nj<n and (ni,nj) not in seen):
                    q.append((ni,nj))
                    dist[ni][nj] = dist[i][j] + 1 
                    seen.add((ni,nj))
        return dist 

# @lc code=end

