#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0 for i in range(n+1)]#相信i的人的个数
        b = [0 for i in range(n+1)]#i相信的人的个数

        for i,j in trust:
            a[j] += 1 
            b[i] += 1
        for i in range(1,n+1):
            if(a[i]==n-1 and b[i]==0):
                return i
        return -1 
# @lc code=end

