class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
        """
        def reverse(nums,i,j):
            while(i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        k = k % len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k-1,len(nums)-1)

if __name__ ==  "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(s.rotate(nums,k))