#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0 
        if end not in bank:
            return -1 
        bank = set(bank)
        q = deque([(start,0)])
        while q:
            cur,step = q.popleft()
            for i,x in enumerate(cur):
                for j in "ACGT":
                    print(i,x,j,bank,cur)
                    if j!=x:
                        nxt = cur[:i] + j + cur[i+1:]
                        print(nxt)
                        if nxt in bank:
                            if nxt == end:
                                return step + 1 
                            bank.remove(nxt)
                            q.append((nxt,step+1))
        return -1 

# @lc code=end

