#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        ans = []
        for i in range(len(sentence)):
            if(sentence[i][0].lower() in "aeiou"):
                sentence[i] = sentence[i]+ "ma"
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0]
                sentence[i] = sentence[i]+ "ma"
            sentence[i] = sentence[i] + "a"*(i+1) 
            ans.append(sentence[i])
        return " ".join(ans)  
# @lc code=end

