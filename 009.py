# # coding=utf-8
# import sys
# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0 or (x ! = 0 and x%10 == 0):
#             return False
#         else:
#             val = 0
#             tem = x
#             while(val < tem):
#                 val = val * 10 + tem % 10
#                 tem = tem // 10
#             return val == tem or  val//10 == tem
# def main():
#     x = 10
#     a = Solution()
#     print(a.isPalindrome(x))
# main()
class Solution:
    def isPalindrome(self, x):
        if(x<0 or (x!=0 and x %10 ==0)):
            return False
        num = 0 
        x = str(x)
        for i in range(int(len(x)/2)):
            if(x[i]==x[-i-1]):
                num = num+1
        if num == int(len(x)/2):
            return True
        else:
            return False
if __name__ == "__main__":
    x = Solution()
    print(x.isPalindrome(1214431312))
















