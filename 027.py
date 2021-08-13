
class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     i,n = 0,len(nums)
    #     for j in range(n):
    #         if nums[j] != val:
    #             nums[i] = nums[j]
    #             i += 1
    #     return i
    
    '''
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    '''
    def removeElement(self, nums, val):
        nums.sort()
        j = len(nums)-1
        c_nums = 0                   
        for i in range(len(nums)):
            if nums[i] == val:
                c_nums += 1
        a_nums = c_nums
        for i in range(len(nums)):
            if nums[i] == val:
                    nums[i] = nums[j] 
                    nums[j] = val 
                    j = j-1
                    c_nums -= 1
                    if c_nums == 0:
                        break
        return (len(nums)-a_nums)


if __name__ ==  "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(s.removeElement(nums,2))