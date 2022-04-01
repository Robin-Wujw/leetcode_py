#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # result = []
        # for i in range(left,right+1):
        #     num = i 
        #     while(i/10!=0):
        #         a = i % 10
        #         if(a==0):
        #             break
        #         if(num%a!=0 ):
        #             break
        #         i = i // 10
        #         if(i/10==0):
        #             result.append(num)
        # return result    
        def isSelfDividing(num: int) -> bool:
            x = num
            while x:
                x, d = divmod(x, 10)
                if d == 0 or num % d:
                    return False
            return True
        return [i for i in range(left, right + 1) if isSelfDividing(i)]


# @lc code=end

