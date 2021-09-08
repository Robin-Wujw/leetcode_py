class Solution:
    def numTrees(self, n: int) -> int:
        """
        给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
        输入：n = 3
        输出：5
        输入：n = 1
        输出：1
        """
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]

if __name__ ==  "__main__":
    s = Solution()
    n = 5
    print(s.numTrees(n))
