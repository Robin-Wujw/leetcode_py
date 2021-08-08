# class Solution:
#     def fourSum(self,nums,target):
#         """

#         :type nums:  List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """

#         ret,dict = set(),{}
#         numsLen  = len(nums)
#         nums.sort()
#         for i in range(numsLen):
#             for j in range(i+1,numsLen):
#                 key = nums[i] + nums[j]
#                 if key not in dict.keys():
#                     dict[key]=[(i,j)]
#                 else:
#                     dict[key].append((i,j))

#         for i in range(numsLen):
#             for j in range(i+1,numsLen):
#                 temp = target - nums[i] - nums[j]
#                 if temp in dict.keys():
#                     for tempIndex in dict[temp]:
#                         if tempIndex[0] > j:
#                             ret.add((nums[i],nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]])))
#         return [list(i) for i in ret]
class Solution:
    # 输入：nums = [1,0,-1,0,-2,2], target = 0
    # [-2,-1,0,0,1,2]
    # 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    def fourSum(self, nums, target):     
        results = []
        nums.sort()
        for index_a,a in enumerate(nums):
            #选择a时候的去重
            if index_a >=1 and nums[index_a-1] == a:
                continue
            for index_b in range(index_a+1,len(nums)):
                b = nums[index_b]
                if index_b >index_a+1 and nums[index_b-1] == b:
                    continue
                left = index_b + 1 
                right = len(nums)-1
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    total = a + b + c + d
                    if target - total > 0:
                        left = left + 1
                    elif target - total < 0:
                        right = right-1
                    else:
                        results.append([a,b,c,d])
                        print(a,b,left,right)
                        # a确定之后，后面的left和right指向的元素去重
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right-=1
                        left  += 1
                        right -= 1
        return results
if __name__ =="__main__":
    s = Solution()
    nums = [2,2,2,2,2]
    target = 8
    print(s.fourSum(nums,target))
