#
# @lc app=leetcode.cn id=2055 lang=python3
#
# [2055] 蜡烛之间的盘子
#

# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        presum,sum = [0] * n,0
        left,l = [0] * n, -1 
        for i,ch in enumerate(s):
            if(ch=="*"):
                sum += 1 
            else:
                l = i 
            presum[i] = sum #预处理
            left[i] = l #表示从左到右是否有蜡烛
        right,r = [0] * n, -1 
        for i in range(n-1,-1,-1):
            if(s[i]=="|" ):
                r = i 
            right[i] = r
        ans = [0] * len(queries)
        for i,(x,y) in enumerate(queries):
            x , y = right[x] , left[y]
            if x >=0 and y >=0 and y>=x:
                ans[i] = presum[y] - presum[x]
        return ans

# @lc code=end

