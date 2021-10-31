class Solution:
    def lengthOfLIS(self, nums):
        """
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
        子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。    
        """
        
        dp = [1 for i in range(len(nums)+1)]
        num = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if(nums[i]>nums[j]):
                    dp[i] = max(dp[i],dp[j]+1)
                    num = max(num,dp[i])
        return num
# class Solution:
# 二分查找法 最长递增子序列和一种叫做 patience game 的纸牌游戏有关，甚至有一种排序方法就叫做 patience sorting（耐心排序）。
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         d = []
#         for n in nums:
#             if not d or n > d[-1]:
#                 d.append(n)
#             else:
#                 l, r = 0, len(d) - 1
#                 loc = r
#                 while l <= r:
#                     mid = (l + r) // 2
#                     if d[mid] >= n:
#                         loc = mid
#                         r = mid - 1
#                     else:
#                         l = mid + 1
#                 d[loc] = n
#         return len(d)
if __name__ ==  "__main__":
    a = Solution()
    n = [0,3,1,6,2,2,7]
    print(a.lengthOfLIS(n))