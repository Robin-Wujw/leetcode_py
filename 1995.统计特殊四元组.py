#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#

# @lc code=start


from typing import Counter

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # num = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             temp_sum = nums[i] + nums[j] + nums[k]
        #             if(temp_sum in nums[k:]):
        #                 num += nums[k:].count(temp_sum) 
        # return num
        n = len(nums)
        ans = 0
        cnt = Counter()
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                cnt[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                if (total := nums[a] + nums[b]) in cnt:
                    ans += cnt[total]
        return ans
# @lc code=end

