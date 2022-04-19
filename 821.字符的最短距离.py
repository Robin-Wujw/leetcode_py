#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [0 for i in range(n)]
        
        idx = -n
        for i,ch in enumerate(s):
            if ch == c:
                idx = i
            answer[i] = i - idx
        idx = 2*n
        for i in range(n-1,-1,-1):
            if s[i] == c:
                idx = i
            answer[i] = min(idx-i,answer[i])
        return answer
# @lc code=end

