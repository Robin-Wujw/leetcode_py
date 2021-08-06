# class Solution:
#     def __init__(self):
#         self.longestSize = 0
#         self.longestStart = 0

#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype:  str
#         """
#         for index, value in enumerate(s):
#             self.checkOddPalindrome(s, index)
#             self.checkEvenPalindrome(s, index)
#         return s[self.longestStart:self.longestStart + self.longestSize + 1]

#     def checkOddPalindrome(self, s, index):
#         start = index
#         end = index
#         while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1]:
#             start -= 1
#             end += 1
#         if end - start > self.longestSize:
#             self.longestSize = end - start
#             self.longestStart = start

#     def checkEvenPalindrome(self, s, index):
#         start = index
#         end = min(index + 1, len(s) - 1)
#         while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1] and s[start] == s[end]:
#             start -= 1
#             end += 1
#         if end - start > self.longestSize and s[start] == s[end]:
#             self.longestSize = end - start
#             self.longestStart = start
class Solution:
    #采用双指针法，从中央向两边延伸
    '''
    s = "babad"  输出 bab
    s = "cbbd"   输出 bb
    '''
    def __init__(self):
        self.left = 0
        self.right = 0
        self.maxlen = 0
    def longestPalindrome(self,s):
        for i in range(len(s)):
            self.extend(s,i,i,len(s)) 
            self.extend(s,i,i+1,len(s))
        return s[self.left:self.right+1]

    def extend(self,s,i,j,len):
        while(i>=0 and j < len and s[i]==s[j]):
            if(j-i+1 > self.maxlen):
                self.left = i
                self.right = j 
                self.maxlen = j-i+1
            i -= 1
            j += 1
if __name__ == "__main__":
    s = Solution()
    st = "babad"
    print(s.longestPalindrome(st))
