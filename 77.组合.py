#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n,k,startIndex):
            if(len(path)==k):
                print(path)
                res.append(path[:])
                return 
            for i in range(startIndex,n+1):
                path.append(i)
                backtrack(n,k,i+1)
                path.pop()
        backtrack(n,k,1)
        return res
            
# @lc code=end

