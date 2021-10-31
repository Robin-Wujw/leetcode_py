class Solution:
    def twoSum(self, nums, target):
        """
        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
        你可以按任意顺序返回答案。
        """
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