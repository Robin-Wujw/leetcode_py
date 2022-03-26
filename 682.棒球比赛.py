#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # num = []
        # for i in ops:
        #     if(i =="C"):
        #         num = num[:-1]
        #     elif(i=="D"):
        #         num.append(num[-1]*2)
        #     elif(i=="+"):
        #         num.append(num[-1]+num[-2])
        #     else:
        #         num.append(int(i))
        # return sum(num)
        nums = [0] * 1010
        idx = 0
        for x in ops:
            if x == '+':
                nums[idx] = nums[idx - 1] + nums[idx - 2]
            elif x == 'D':
                nums[idx] = nums[idx - 1] * 2
            elif x == 'C':
                idx -= 2
            else:
                nums[idx] = int(x)
            idx += 1
        return sum(nums[:idx])

# @lc code=end

