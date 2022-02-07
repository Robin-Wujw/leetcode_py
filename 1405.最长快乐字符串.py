#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret = []
        ans = [[a,'a'],[b,'b'],[c,'c']]
        while True:
            ans.sort(key=lambda x: -x[0])
            hasNext = False
            for i,(c,ch) in enumerate(ans):
                if(c<=0):
                    break
                if(len(ch)>=2 and ch[-1]==ch and ch[-2]==ch):
                    break
                hasNext = True
                ret.append(ch)
                ans[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ret)

# @lc code=end

