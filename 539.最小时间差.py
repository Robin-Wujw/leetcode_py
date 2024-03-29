#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
def getMinutes(t: str) -> int:
    return ((ord(t[0]) - ord('0')) * 10 + ord(t[1]) - ord('0')) * 60 + (ord(t[3]) - ord('0')) * 10 + ord(t[4]) - ord('0')

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        if n > 1440:
            return 0
        timePoints.sort()
        ans = float('inf')
        t0Minutes = getMinutes(timePoints[0])
        preMinutes = t0Minutes
        for i in range(1, n):
            minutes = getMinutes(timePoints[i])
            ans = min(ans, minutes - preMinutes)  # 相邻时间的时间差
            preMinutes = minutes
        ans = min(ans, t0Minutes + 1440 - preMinutes)  # 首尾时间的时间差
        return ans
# @lc code=end

