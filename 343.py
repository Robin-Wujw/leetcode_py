class Solution:
    """
    给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

    示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。
    示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    说明: 你可以假设 n 不小于 2 且不大于 58。
    """
    def integerBreak(self, n):
        dp = [0 for i in range(n+1)]
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],max((i-j)*j,dp[i-j]*j))
        return dp[-1]
if __name__ ==  "__main__":
    a = Solution()
    n = 10
    print(a.integerBreak(10))