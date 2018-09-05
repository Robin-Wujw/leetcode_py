class Solution:
    def twoSum(self,nums,target):
        theOtherDict = {}
        for index , item in enumerate(nums):
            if item in theOtherDict:
                return [theOtherDict, index]
            else:
                theOtherDict[target-item] = index
