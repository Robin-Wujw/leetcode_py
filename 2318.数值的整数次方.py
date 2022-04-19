# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(N):
            if(N==0):
                return 1
            y = quickPow(N//2)
            return y*y if(N%2==0) else y*y*x
        return quickPow(n) if(n>=0) else 1/quickPow(-n)