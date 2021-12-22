#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            print(j)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            print(rightDistance)
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            print(leftDistance)
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans
# @lc code=end

