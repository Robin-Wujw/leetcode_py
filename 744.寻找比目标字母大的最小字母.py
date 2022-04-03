#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if(ord(target) >= ord(letters[-1])):
            return letters[0]
        for i in range(len(letters)):
            if(ord(target)<ord(letters[i])):
                return letters[i] 
            elif(ord(target)==ord(letters[i])):
                for j in range(i,len(letters)):
                    if(letters[j] != letters[i]):
                        return letters[j]
        
# @lc code=end

