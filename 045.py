class Solution:
    def jump(self, nums):
        """
        给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。
        你的目标是使用最少的跳跃次数到达数组的最后一个位置。
        假设你总是可以到达数组的最后一个位置。
        输入: nums = [2,3,1,1,4]
        输出: 2
        """
        curmax = 0 
        ans = 0
        nextmax = 0
        for i in range(len(nums)-1):
            nextmax = max(i+nums[i],nextmax)
            if(i==curmax):
                curmax = nextmax 
                ans += 1
                if(nextmax>=len(nums)-1): break 
        return ans


if __name__ ==  "__main__":
    s = Solution()
    nums = [5]
    print(s.jump(nums))