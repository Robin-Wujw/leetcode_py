class Solution:
    def permute(self, nums):
        '''
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        '''
        n = len(nums)
        l = nums 
        ret = []

        def conflict(t):
            return False
        
        def backtrack(t):
            if(t>=n):
                ret.append(l[:])
            else:
                for i in range(t,n):
                    self.l[t],self.l[i] = self.l[i],self.l[t]
                    if not conflict(t):
                        backtrack(t+1)
                    self.l[i],self.l[t] = self.l[t],self.l[i]
        backtrack(0)
        return ret