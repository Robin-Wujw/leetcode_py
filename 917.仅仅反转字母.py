#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # ans = list(s)
        # i,j = 0,len(s)-1
        # while(i<j):
        #     while(not('a'<=s[i]<='z' or 'A'<=s[i]<='Z') and i<j):
        #         i += 1 
        #     while(not('a'<=s[j]<='z' or 'A'<=s[j]<='Z')and i<j):
        #         j -= 1
        #     ans[i],ans[j] = ans[j],ans[i]
        #     i += 1
        #     j -= 1 
        # return ''.join(ans)
        ans = list(s)
        left, right = 0, len(ans) - 1
        while True:
            while left < right and not ans[left].isalpha():  # 判断左边是否扫描到字母
                left += 1
            while right > left and not ans[right].isalpha():  # 判断右边是否扫描到字母
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)


# @lc code=end

