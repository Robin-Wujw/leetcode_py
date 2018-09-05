class Solution:
    def __init__(self):
        self.longestSize = 0
        self.longestStart = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype:  str
        """
        for index, value in enumerate(s):
            self.checkOddPalindrome(s, index)
            self.checkEvenPalindrome(s, index)
        return s[self.longestStart:self.longestStart + self.longestSize + 1]

    def checkOddPalindrome(self, s, index):
        start = index
        end = index
        while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1]:
            start -= 1
            end += 1
        if end - start > self.longestSize:o
            self.longestSize = end - start
            self.longestStart = start

    def checkEvenPalindrome(self, s, index):
        start = index
        end = min(index + 1, len(s) - 1)
        while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1] and s[start] == s[end]:
            start -= 1
            end += 1
        if end - start > self.longestSize and s[start] == s[end]:
            self.longestSize = end - start
            self.longestStart = start
9o