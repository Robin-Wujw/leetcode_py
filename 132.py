class Solution:
    def minCut(self, s):
        '''
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
        返回符合要求的 最少分割次数。
        '''
        isPalindromic=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or isPalindromic[i+1][j-1]): 
                    isPalindromic[i][j] = True
        
        dp = [i for i in range(len(s))]
        for i in range(1,len(s)):
            if(isPalindromic[0][i]):
                dp[i] = 0
                continue
            for j in range(0,i):
                if(isPalindromic[j+1][i]):
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]
if __name__ ==  "__main__":
    s = Solution()
    a = "aab"
    print(s.minCut(a))