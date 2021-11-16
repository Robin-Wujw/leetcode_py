#
# @lc app=leetcode.cn id=977 lang=python3
#给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# [977] 有序数组的平方
#
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # ret = []
        # if(nums[-1]>-nums[0]):
        #     result = [0] * (nums[-1]+1)
        # else:
        #     result = [0] * (-nums[0]+1)
        # for i in nums:
        #     if i < 0:
        #         result[-i] += 1
        #     else:
        #         result[i]  += 1
        # for i in range(len(result)):
        #     if(result[i]!=0):
        #         while(result[i]!=0):
        #             ret.append(i*i)
        #             result[i] -= 1
        # return ret
        n = len(nums)
        i,j,k = 0,n - 1,n - 1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans
# @lc code=end

