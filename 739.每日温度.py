#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
from typing import Deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = Deque()
        day   = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while(queue and temperatures[i] > temperatures[queue[-1]]):
                    index = queue.pop()
                    day[index] = i - index 
            queue.append(i)      
        return day 
                
# @lc code=end

