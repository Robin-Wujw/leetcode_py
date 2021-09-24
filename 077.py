class Solution:
    def combine(self, n, k):
        '''
        给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

        你可以按 任何顺序 返回答案。

        '''
        l = []
        res = []
        def backtrack(n,k,startIndex):
            if len(l) == k:
                res.append(l[:])
                return 
            for i in range(startIndex,n+1): # for i in range(startIndex,n-(k-len(path))+2):  #优化的地方-->剪枝
                l.append(i)
                backtrack(n,k,i+1)
                l.pop()
        backtrack(n,k,1)
        return res

if __name__ ==  "__main__":
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n,k))