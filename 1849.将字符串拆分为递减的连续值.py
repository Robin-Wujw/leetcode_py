#
# @lc app=leetcode.cn id=1849 lang=python3
#
# [1849] 将字符串拆分为递减的连续值
#

# @lc code=start
class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        start = 0
        # 枚举第一个子字符串对应的初始值
        # 第一个子字符串不能包含整个字符串
        for i in range(n - 1):
            start = 10 * start + int(s[i])
            # 循环验证当前的初始值是否符合要求
            pval = start
            cval = 0
            cidx = i + 1
            for j in range(i + 1, n):
                if pval == 1:
                    # 如果上一个值为 1，那么剩余字符串对应的数值只能为 0
                    if all(s[k] == '0' for k in range(cidx, n)):
                        return True
                    else:
                        break
                cval = 10 * cval + int(s[j])
                if cval > pval - 1:
                    # 不符合要求，提前结束
                    break
                elif cval == pval - 1:
                    if j + 1 == n:
                        # 已经遍历到末尾
                        return True
                    pval = cval
                    cval = 0
                    cidx = j + 1     
        return False
            
# @lc code=end

