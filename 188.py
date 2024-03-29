class Solution:
    def maxProfit(self, k: int, prices):
        """
        给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。      
        """
        if(len(prices)==0):
            return 0
        n = len(prices)
        dp = [[0] * (2*k+1) for i in range(n)]
        i = 1
        while(i<(2*k+1)):
            dp[0][i] = -prices[0]
            i+=2
        print(dp)
        for i in range(1,n):
            for j in range(0,2*k-1,2):
                dp[i][j+1] = max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[-1][2*k]
if __name__ ==  "__main__":
    s = Solution()
    prices  = [3,2,6,5,0,3]
    print(s.maxProfit(2,prices))