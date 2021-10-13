class Solution:
    def minSubArrayLen(self, target: int, nums):
        """
        给定一个含有 n 个正整数的数组和一个正整数 target 。
        找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
        """
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while(Sum>=target):
                res = min(res,i-index+1)
                Sum -= nums[i]
                index += 1
if __name__ ==  "__main__":
    a = Solution()
    target = 7 
    nums = [2,3,1,2,4,3]
    print(a.minSubArrayLen(target,nums))