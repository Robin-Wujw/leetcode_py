# class Solution(object):
#     def letterCombinations(self,digits):
#         """

#         :type digits:  str
#         :return:       List{str}
#         """
#         keyMap = {
#             "0": " ",
#             "1": "*",
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#         results = []
#         for digit in digits:
#             if len(results) == 0 :
#                 for letter in keyMap[digit]:
#                     results.append(letter)
#             else:
#                 tempResults = []
#                 for result in results:
#                     for letter in keyMap[digit]:
#                         tempResults.append(result + letter)
#                 results = tempResults
#         return results

class Solution:
    def letterCombinations(self, digits):
        num_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.s = ""
        res = []
        if len(digits) == 0 : return res 
        def backtrack(digits,index):
            if index == len(digits): return res.append(self.s)
            digit =digits[index]
            letters = num_dic[digit]
            for letter in letters:
                self.s = self.s + letter
                backtrack(digits,index+1)
                self.s = self.s[:-1]
        backtrack(digits,0)
        return res

if __name__ =="__main__":
    s = Solution()
    st = '423'
    print(s.letterCombinations(st))
