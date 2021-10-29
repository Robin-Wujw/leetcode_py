class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        输入: [0,1,0,3,12]
        输出: [1,3,12,0,0]
        """
        slow = 0
        if nums==None or nums.length <=1:
            return
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0