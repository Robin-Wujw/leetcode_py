class Solution:
    def climbStairs(self, n):
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        """
        if (n <= 1): return n
        dp = [0] * (n+1) 
        dp[1] = 1
        dp[2] = 2 
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    # 法二
    # dp[i]表示爬到第i级楼梯的种数， (1, 2) (2, 1)是两种不同的类型
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # for i in range(n+1):
        #     for j in range(1, 3): #把3换为m+1 就可适用 一次蹦1到m阶楼梯的情况
        #         if i>=j:
        #             dp[i] += dp[i-j]
        # return dp[-1]

if __name__ ==  "__main__":
    s = Solution()
    n = 3
    print(s.climbStairs(n))