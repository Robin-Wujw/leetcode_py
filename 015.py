class Solution:
    def threeSum(self,nums):
        """

        :type nums: List[int]
        :return: List[List[int]]
        n^2
        [-4,-1,-1,0,1,2,2]
        results = []
        for index in nums:
            a = nums[index]
            left = index +1
            right= len(nums)-1
            while(left>right)
                b=nums[left]
                c=nums[right]
                total= a+b+c
                if total ==0
                    add one result into results
                    left++ until different number
                    right--
                elif total < 0:
                    left++
                elif total > 0:
                    right--
        """
        results = []
        nums.sort()
        for index,a in enumerate(nums):
            if index >=1 and nums[index-1] == a:
                continue
            left,right = index+1,len(nums) - 1
            while left<right:
                b = nums[left]
                c = nums[right]
                total = a+b+c
                if total <0:
                    left +=1
                elif total>0:
                    right-=1
                else:
                    results.append([a,b,c])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left +=1
                    right-=1
        return results