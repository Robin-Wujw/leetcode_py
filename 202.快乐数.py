#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false。
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def caculatesum(num):
            _sum = 0 
            while(num):
                _sum += (num % 10)**2       
                num = num // 10 
            return _sum
        number = set()
        while(True):
            n = caculatesum(n)
            if(n==1):
                return True
            if n in number:
                return False
            else:
                number.add(n)
# @lc code=end

