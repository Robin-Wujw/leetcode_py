class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<2:
            return len(nums)
        i = 1 
        j = 0 
        while(i<len(nums)):
            if(nums[j]!=nums[i]):
                j += 1
                nums[j] = nums[i]
            i = i+1
        return j+1,nums
if __name__== "__main__":   
    s = Solution()
    nums= [1,1,2,4,4,6,8,9,9,9]
    print(s.removeDuplicates(nums))

                