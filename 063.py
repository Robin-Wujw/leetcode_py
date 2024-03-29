class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
        '''
        #动态规划法
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        for i in range(1,m):
            if(obstacleGrid[i][0])==1:
                continue
            else:
                dp[i][0] = dp[i-1][0] #每初始行 每初始列 如果中间出了障碍就过不去了
        for j in range(1,n):
            if(obstacleGrid[0][j])==1:
                continue
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]



if __name__ ==  "__main__":
    s = Solution()
    obstacleGrid = [[0,0],[1,1],[0,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))