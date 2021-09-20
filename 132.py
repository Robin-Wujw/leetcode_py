class Solution:
    def minCut(self, s):
        '''
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
        返回符合要求的 最少分割次数。
        '''
        # path = []
        # result = []
        # def backtrack(s,startIndex):
        #     if(startIndex>=len(s)):
        #         return result.append(path[:])
        #     for i in range(startIndex,len(s)):
        #         l = s[startIndex:i+1]
        #         if(l==l[::-1]):path.append(l[:])
        #         else: continue
        #         backtrack(s,i+1)
        #         path.pop()
        # backtrack(s,0)
        # ret = 100000000
        # for i in result:
        #     ret = min(len(i)-1,ret)
        # return ret
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
    print(s.minCut(a))