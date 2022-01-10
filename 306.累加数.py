#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
    #穷举
        n = len(num)
        for secondStart in range(1, n-1):
            if num[0] == '0' and secondStart != 1:
                break
            for secondEnd in range(secondStart, n-1):
                if num[secondStart] == '0' and secondStart != secondEnd:
                    break
                if self.valid(secondStart, secondEnd, num):
                    return True
        return False
    
    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        n = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd <= n - 1:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= n or num[thirdStart:thirdEnd+1] != third:
                break
            if thirdEnd == n-1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False
    
    def stringAdd(self, s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third = []
        carry, cur = 0, 0
        while firstEnd >= firstStart or secondEnd >= secondStart or carry != 0:
            cur = carry
            if firstEnd >= firstStart:
                cur += ord(s[firstEnd]) - ord('0')
                firstEnd -= 1
            if secondEnd >= secondStart:
                cur += ord(s[secondEnd]) - ord('0')
                secondEnd -= 1
            carry = cur // 10
            cur %= 10
            third.append(chr(cur + ord('0')))
        return ''.join(third[::-1])
#字符串加法+dfs
        # def helper(a, b):
        #     i, j, res, one = len(a) - 1, len(b) - 1, [], 0
        #     while i >= 0 or j >= 0:
        #         curA = curB = 0
        #         if i >= 0:
        #             curA = int(a[i])
        #             i -= 1
        #         if j >= 0:
        #             curB = int(b[j])
        #             j -= 1
        #         cur = curA + curB + one
        #         if cur >= 10:
        #             cur %= 10
        #             one = 1
        #         else:
        #             one = 0
        #         res.append(str(cur))
        #     if one:
        #         res.append("1")
        #     return "".join(res[::-1])
        
        # def dfs(p, q):
        #     last, first, second = 0, p, q
        #     while second < len(num):
        #         if (num[last] == '0' and first > last + 1) or (num[first] == '0' and second > first + 1):
        #             return False
        #         s = helper(num[last:first], num[first:second])
        #         if num[second:second+len(s)] != s:
        #             return False
        #         last, first, second = first, second, second + len(s)
        #     return True
        
        # for i in range(1, len(num) - 1):
        #     for j in range(i + 1, len(num)):
        #         if dfs(i, j):
        #             return True
        # return False
# @lc code=end

