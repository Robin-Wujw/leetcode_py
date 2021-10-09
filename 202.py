class Solution:
    def isHappy(self, n):
        def calculate_happy(num):
            sum_ = 0
            
            # 从个位开始依次取，平方求和
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_
        number = set()
        while(True):
            n = calculate_happy(n)
            if(n==1):
                return True
            if(n in number):
                return False
            else:
                number.add(n)
if __name__ ==  "__main__":
    s = Solution()
    nums = 19
    print(s.isHappy(nums))