import sys 
class Solution:
    def maxProfit(self, prices) -> int:
        """
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
        """
        # low = sys.maxsize
        # result = 0
        # for i in range(len(prices)):
        #     low = min(low,prices[i])
        #     result = max(result,prices[i]-low)
        # return result
        if(len(prices)==0):
            return 0
        n = len(prices)
        dp = [[0] * n for i in range(n)]
        # dp = [[0] * 2 for _ in range(n)]
        print(dp)
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,n):
            dp[i][0] = max(-prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][1],prices[i]+dp[i][0])
        return dp[-1][1]
        

if __name__ ==  "__main__":
    s = Solution()
    prices = [7]
    print(s.maxProfit(prices))