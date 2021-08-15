class Solution:
    def searchInsert(self, nums, target):
        '''
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

        请必须使用时间复杂度为 O(log n) 的算法。
        输入: nums = [1,3,5,6], target = 5
        输出: 2
        '''
        n = len(nums)
        left = 0 
        right = n - 1
        while(left <= right):
            middle = left + (right - left)// 2
            if(nums[middle]<target):
                left = middle + 1 
            if(nums[middle]>target):
                right = right - 1
            if(nums[middle]== target):
                return middle 
        return right + 1

if __name__ ==  "__main__":
    s = Solution()
    nums = [1,3,5,6]
    target = 2
    print(s.searchInsert(nums,target))