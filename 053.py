class Solution:
    def maxSubArray(self, nums):
        '''
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出：6
        解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
        '''
        # #贪心法
        # result = -float('inf')
        # count = 0  
        # for i in range(len(nums)):
        #     count += nums[i]
        #     if(result<count):
        #         result = count
        #     if(count<=0):
        #         count = 0 
        # return result
        # 动态规划法
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result

if __name__ ==  "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
