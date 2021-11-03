class Solution:
    def rob(self, nums) -> int:
        """
        你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
        给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
        """
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        dp = [0]*(len(nums))
        max_n = self.max_m(nums,dp,0,len(nums)-2)
        max_n2 = self.max_m(nums,dp,1,len(nums)-1)
        return max(max_n,max_n2)

    def max_m(self,nums,dp,start,end):
        if end == start: return nums[start]
        dp[start] = nums[start]
        print(start,end)
        dp[start+1] = max(nums[start],nums[start+1])
        for i in range(start+2,end+1):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[end]
if __name__ ==  "__main__":
    s = Solution()
    nums = [1,1]
    print(s.rob(nums))