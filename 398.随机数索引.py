#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
from collections import defaultdict
from random import choices


class Solution:

    def __init__(self, nums: List[int]):
        self.ret = defaultdict(list)
        for i,x in enumerate(nums):
            self.ret[x].append(i)



    def pick(self, target: int) -> int:
        return choice(self.ret[target])



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

