#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # dict = {}
        # ret  = 100000
        # for i in text:
        #     if(i not in dict):
        #         dict[i] = 1
        #     else:
        #         dict[i] += 1 
        
        # for i in dict:
        #     if('b' not in dict or 'a' not in dict or 'l' not in dict or 'o' not in dict or 'n' not in dict ):
        #         return 0
        #     if(i=='b' or i=='a' or i=='n'):
        #         ret = min(ret,dict[i])
        #     elif(i=='l' or i=='o'):
        #         ret = min(ret,int(dict[i]/2))
        # return ret 
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(ch for ch in text if ch in "balon")
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values()) if len(cnt) == 5 else 0


# @lc code=end

