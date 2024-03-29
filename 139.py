class Solution:
    def wordBreak(self, s, wordDict):
        """
        给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
        说明：
        拆分时可以重复使用字典中的单词。
        你可以假设字典中没有重复的单词。
        输入: s = "applepenapple", wordDict = ["apple", "pen"]
        输出: true
        解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
             注意你可以重复使用字典中的单词。
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if(i>=len(word)):
                    print(dp[i-len(word)],s[i-len(word):i])
                    dp[i] = dp[i] or (dp[i-len(word)] and s[i-len(word):i]==word)
        return dp[-1]



if __name__ ==  "__main__":
    a = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(a.wordBreak(s,wordDict))