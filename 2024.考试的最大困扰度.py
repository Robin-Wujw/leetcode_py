#
# @lc app=leetcode.cn id=2024 lang=python3
#
# [2024] 考试的最大困扰度
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxCL(ch):
            ans,sum,left = 0,0,0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while(sum>k):
                    sum -= answerKey[left] !=ch
                    left += 1
                ans = max(ans,right-left+1)
            return ans
        return max(maxCL('T'),maxCL('F'))  

# @lc code=end

