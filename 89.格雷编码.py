#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
    #1 对称生成
        ans = [0]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans
        
# @lc code=end

