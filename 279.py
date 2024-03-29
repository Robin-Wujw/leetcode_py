import cmath
class Solution:
    def numSquares(self, n: int) -> int:
        """
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
        给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
        完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
        """
        nums = [i**2 for i in range(1,n+1)if(i**2<=n)]
        dp = [10000 for i in range(1,n+2)]
        dp[0] = 0
        for i in range(1,n+1):
            for num in nums:
                if(i>=num):
                    dp[i] = min(dp[i-num]+1,dp[i])
        return dp[-1]
if __name__ ==  "__main__":
    a = Solution()
    n = 12
    print(a.numSquares(n))