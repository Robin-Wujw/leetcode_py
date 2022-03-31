#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right+1):
            num = i 
            while(i/10!=0):
                a = i % 10
                if(a==0):
                    break
                if(num%a!=0 ):
                    break
                i = i // 10
                if(i/10==0):
                    result.append(num)
        return result    

# @lc code=end

