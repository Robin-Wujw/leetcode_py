class Solution:
    def coinChange(self, coins, amount):
        """
        给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
        计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
        你可以认为每种硬币的数量是无限的。
        """
        dp = [10000 for i in range(1,amount+2)]
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if(coin <= i):
                    print(i,coin,dp[i],dp[i-coin])
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[-1] == 10000: dp[i] = -1
        return dp[-1]


if __name__ ==  "__main__":
    a = Solution()
    coins = [2]
    amount = 3
    print(a.coinChange(coins,amount))