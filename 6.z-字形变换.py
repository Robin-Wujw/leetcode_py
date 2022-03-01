#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # n, r = len(s), numRows
        # if r == 1 or r >= n:
        #     return s
        # t = r * 2 - 2
        # ans = []
        # for i in range(r):  # 枚举矩阵的行
        #     for j in range(0, n - i, t):  # 枚举每个周期的起始下标
        #         ans.append(s[j + i])  # 当前周期的第一个字符
        #         if 0 < i < r - 1 and j + t - i < n:
        #             ans.append(s[j + t - i])  # 当前周期的第二个字符
        # return ''.join(ans)
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1  # 向下移动
            else:
                x -= 1
                y += 1  # 向右上移动
        return ''.join(ch for row in mat for ch in row if ch)
# @lc code=end

