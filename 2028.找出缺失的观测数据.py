#
# @lc app=leetcode.cn id=2028 lang=python3
#
# [2028] 找出缺失的观测数据
#

# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_ = (n+m)*mean
        mean_ = (sum_-sum(rolls))//n
        missingSum = mean * (n + len(rolls)) - sum(rolls)
        if not n <= missingSum <= n * 6:
            return []
        res = []
        return [((sum_-sum(rolls))//n)+1] * (sum_-sum(rolls))%n  + [((sum_-sum(rolls))//n)] * (n-(sum_-sum(rolls))%n)
        # missingSum = mean * (n + len(rolls)) - sum(rolls)
        # if not n <= missingSum <= n * 6:
        #     return []
        # quotient, remainder = divmod(missingSum, n) #商和余数
        # #相当于前面missingSum%n个数是 quotient +1 后面是quotient
        # return [quotient + 1] * remainder + [quotient] * (n - remainder)

                
# @lc code=end

