#
# @lc app=leetcode.cn id=383 lang=python3
#给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in ransomNote:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in magazine:
            if i in dict and dict[i]!=0:
                dict[i] -= 1
            else: continue
        for i in dict.values():
            if i!= 0:
                return False 
        return True
# @lc code=end

