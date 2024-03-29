class Solution:
    def partition(self, s):
        '''
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
        回文串 是正着读和反着读都一样的字符串。
        '''
        path = []
        result = []
        def backtrack(s,startIndex):
            if(startIndex>=len(s)):
                return result.append(path[:])
            for i in range(startIndex,len(s)):
                l = s[startIndex:i+1]
                if(l==l[::-1]):path.append(l[:])
                else: continue
                backtrack(s,i+1)
                path.pop()
        backtrack(s,0)
        return result

        

if __name__ ==  "__main__":
    s = Solution()
    a = "aab"
    print(s.partition(a))