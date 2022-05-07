#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

# @lc code=start
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1,n+1))
        while(len(queue)>1):
            for _ in range(k-1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]
# @lc code=end

