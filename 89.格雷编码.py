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

    #2 二进制数转格雷码
        # ans = [0] * (1 << n)
        # for i in range(1 << n):
        #     ans[i] = (i >> 1) ^ i
        # return ans
        
# @lc code=end

