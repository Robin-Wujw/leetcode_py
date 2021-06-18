# import sys

# class Solution(object):
#     def reverse(self,x):
#         """
#         :type x: int
#         :rtype : int
#         """
#         result = 0
#         if x>0:
#             sign = 1
#         else:
#             sign = -1
#             x    = -x
#         while x>0:
#             value = x%10
#             result= result*10+value
#             x     = int(x/10)
#         if result > 2147483647 or result<-2147483648:
#             return 0
#         return result * sign
# def main(object):
#     a = Solution()
#     x= 321
#     print(a.reverse(x))
class Solution:
    def reverse(self, x):
        sum=a=0
        if(x<0):
            sign = -1
        else:
            sign = 1
        x = x*sign
        while x:
            a = x%10
            sum = sum*10 + a 
            x = int(x/10)
        if(sum<-2**31 or sum>2**31-1):
            return 0
        return (sum*sign)
if __name__ == "__main__":
    S = Solution()
    print(S.reverse(1534236469))