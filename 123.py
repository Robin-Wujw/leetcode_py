class Solution:
    def maxProfit(self, prices):
        """
        给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        """
        if(len(prices)==0):
            return 0
        n = len(prices)
        dp = [[0] * 5 for i in range(n)]
        dp[0][0] = 0           # dp[i][0] 无操作
        dp[0][1] = -prices[0]  # dp[i][1] 表示第i天第一次买入股票持有现金
        dp[0][2] = 0           # 表示第i天第一次卖出
        dp[0][3] = -prices[0]  # dp[i][3] 表示第i天第二次买入股票持有现金
        dp[0][4] = 0           # dp[i][4] 表示第i天第二次买入股票持有现金
        for i in range(1,n):
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[-1][4]
if __name__ ==  "__main__":
    s = Solution()
    prices  = [3,3,5,0,0,3,1,4]
    print(s.maxProfit(prices))