#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for c in "!?',;.":
            paragraph = paragraph.replace(c," ")
        dict = {}
        paragraph = paragraph.split()
        for i in paragraph:
            if(i not in dict):
                dict[i] = 1
            else:
                dict[i] += 1 
        max = 0
        maxi = ' ' 
        for i in dict:
            if(dict[i] > max and i not in banned):
                max  = dict[i] 
                maxi = i
        return maxi 
# @lc code=end

