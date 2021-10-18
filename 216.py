class Solution:
    def combinationSum3(self, k: int, n: int):
        """
        找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        说明：
        所有数字都是正整数。
        解集不能包含重复的组合。 

        输入: k = 3, n = 7
        输出: [[1,2,4]]
        """
        l = []
        res = []

        def backtrack(n,k,sum,startIndex):
            if sum > n: return 
            if len(l) == k and sum == n:
                res.append(l[:])
                return 
            for i in range(startIndex,10): # for i in range(startIndex,n-(k-len(path))+2):  #优化的地方-->剪枝
                if(sum+i<=n):
                    l.append(i)
                    sum = sum + i
                else:
                    continue
                backtrack(n,k,sum,i+1)
                sum -= i
                l.pop()
        backtrack(n,k,0,1)
        return res

if __name__ ==  "__main__":
    s = Solution()
    n = 3
    k = 9
    print(s.combinationSum3(n,k))