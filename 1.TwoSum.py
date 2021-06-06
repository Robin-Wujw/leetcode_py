class Solution:
    def twoSum(self, nums, target):
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(nums[i]+nums[j]==target):
        #             return [nums[i],nums[j]]
        Hash = dict()
        for index,value in enumerate(nums):
            if target-value in Hash:
                return [Hash[target-value],index]
            else:
                Hash[value] = index   
if __name__ == "__main__":
    nums = [1,7,11,2]
    target = 9 
    So = Solution()
    print(So.twoSum(nums,target))