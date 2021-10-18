class Solution:
    def rob(self, nums) -> int:
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