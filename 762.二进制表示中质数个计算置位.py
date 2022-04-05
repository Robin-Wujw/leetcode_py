#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    # def countPrimeSetBits(self, left: int, right: int) -> int:
    #     ret = 0
    #     def trans(num):
    #         one = 0 
    #         while(num):
    #             if(num % 2 == 1):
    #                 one += 1 
    #             num = num // 2
    #         if(one in [2,3,5,7,11,13,17,19,23,29,31]):
    #             return True
    #         else:
    #             return False
    #     for i in range(left,right+1):
    #         if(trans(i)):
    #             ret += 1 
    #     return ret 
    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(self.isPrime(x.bit_count()) for x in range(left, right + 1))

# @lc code=end

