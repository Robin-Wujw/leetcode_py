class Solution:
    def maxProfit(self, prices):
        """
        给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        """
        # result = 0 
        # for i in range(1,len(prices)):
        #     result += max(prices[i]-prices[i-1],0)
        # return result
        if(len(prices)==0):
            return 0
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        # dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]  # dp[i][0] 表示第i天持有股票所得最多现金
        dp[0][1] = 0           # 表示第i天不持有股票所得最多现金
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1]-prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[-1][1]
if __name__ ==  "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))