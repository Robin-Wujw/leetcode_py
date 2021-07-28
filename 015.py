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
        # results = []
        # nums.sort()
        # for index,a in enumerate(nums):
        #     if index >=1 and nums[index-1] == a:
        #         continue
        #     left,right = index+1,len(nums) - 1
        #     while left<right:
        #         b = nums[left]
        #         c = nums[right]
        #         total = a+b+c
        #         if total <0:
        #             left +=1
        #         elif total>0:
        #             right-=1
        #         else:
        #             results.append([a,b,c])
        #             while left < right and nums[left] == nums[left+1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right-1]:
        #                 right -= 1
        #             left +=1
        #             right-=1
        # return results
        results = []
        nums.sort()
        for index,a in enumerate(nums):
            #选择a时候的去重
            if index >=1 and nums[index-1] == a:
               continue
            left = index + 1 
            right = len(nums)-1
            while left < right:
                b = nums[left]
                c = nums[right]
                total = a + b + c
                if total<0:
                    left = left+1
                elif total>0:
                    right = right-1
                else:
                    results.append([a,b,c])
                    print(a,left,right)
                    # a确定之后，后面的left和right指向的元素去重
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left  += 1
                    right -= 1
        return results
if __name__ == "__main__":
    s = Solution()
    nums = [-2,0,0,2,2]
    print(s.threeSum(nums))