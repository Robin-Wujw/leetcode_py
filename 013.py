# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dict = {
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000,
#         }
#         result = 0
#         for c in s:
#             result += dict[c]
#         if s.find("IV") != -1:
#             result -=2
#         if s.find("IX") != -1:
#             result -=2
#         if s.find("XL") != -1:
#             result -=20
#         if s.find("XC") != -1:
#             result -=20
#         if s.find("CD") != -1:
#             result -=200
#         if s.find("CM") != -1:
#             result -=200
#         return result

class Solution:
    def romanToInt(self, s):
        dict = { "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
        num = 0
        for i in range(len(s)):
            if i<len(s)-1 and dict[s[i]]<dict[s[i+1]]:
                num-=dict[s[i]]
            else:
                num+=dict[s[i]]
        return num 
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))

