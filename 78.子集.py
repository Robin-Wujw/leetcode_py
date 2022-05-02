#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n   = len(nums)
        ret = []
        l   = []
        def conflict(k):
            return False #无冲突
        def backtrack(t):
            if(t>=n):
               ret.append(l[:])
            else:
                for i in [0,1]:
                    if(i==1):
                        l.append(nums[t])
                    if not conflict(t):
                        backtrack(t+1)
                    if(i==1):
                        l.pop()
        backtrack(0) 
        return ret    




# @lc code=end

