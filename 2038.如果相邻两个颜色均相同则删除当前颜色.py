#
# @lc app=leetcode.cn id=2038 lang=python3
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#

# @lc code=start
from pyparsing import col


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = 'C', 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[ord(cur) - ord('A')] += 1
        return freq[0] > freq[1]
        # sum = 0 
        # for i in range(1,len(colors)-1):
        #     if(colors[i-1] == colors[i] == colors[i+1]== "A"):
        #         sum+=1
        #     if(colors[i-1] == colors[i] == colors[i+1]== "B"):
        #         sum-=1
        # return sum >0   

# @lc code=end

