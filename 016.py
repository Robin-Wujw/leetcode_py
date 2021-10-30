import sys

class Solution(object):
    def threeSumClosest(self,nums,target):
        """
        给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
        :type nums: List(int)
        :type target: int
        :return:
        """
        nums.sort()
        result = 0
        diff   = sys.maxsize
        for index,a in enumerate(nums):
            left = index +1
            right= len(nums)-1
            while left < right:
                b = nums[left]
                c = nums[right]
                total= a + b + c
                if total == target:
                    return target
                if abs(total - target) < diff:
                    result = total
                    diff   = abs(total-target)
                if total < target:
                    left +=1
                if total > target:
                    right-=1
        return result