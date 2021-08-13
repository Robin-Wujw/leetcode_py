class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,-1,-1):
                if(i<j):
                    if(nums[j]>nums[i]):
                        nums[i],nums[j] = nums[j],nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return nums
        return nums.reverse()
if __name__ ==  "__main__":
    s = Solution()
    nums = [4,2,0,2,3,2,0]
    #预期  [4,2,0,3,0,2,2]
    print(s.nextPermutation(nums))