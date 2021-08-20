class Solution:
    def canJump(self, nums):
        '''
        给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。
        判断你是否能够到达最后一个下标。
        输入：nums = [2,3,1,1,4]
        输出：true
        解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标
        '''
        cover = 0
        if len(nums) == 1: return True
        i = 0
        while(i<=cover): #注意这里是i从0到cover
            cover = max(i+nums[i],cover)
            i = i + 1
            if cover >= len(nums)-1: return True
        return False

if __name__ ==  "__main__":
    s = Solution()
    nums = [0,3,1,1,4]
    print(s.canJump(nums))

