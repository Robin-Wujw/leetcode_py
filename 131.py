class Solution:
    def partition(self, s):
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