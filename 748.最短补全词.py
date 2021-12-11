#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license = ''.join(licensePlate.lower().split(' '))
        num = [str(i) for i in range(0,10)]
        res = [i for i in license  if i not in num]
        ret = []
        for i in words:
            re = res.copy()

            for j in i:
                if(j in re):
                    re.remove(j)
                    if(len(re)==0):
                        ret.append(words)
        ret.sort(key=len)
        return ret[0]
                
# @lc code=end

