#
# @lc app=leetcode.cn id=242 lang=python3
#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = {}
        for i in s:
            if(i not in list):
                list[i] = 1
            else:
                list[i] += 1
        for i in t:
            if(i not in list):
                return False
            else:
                list[i] -= 1
        for key in list.values():
            if(key!=0):
                return False
            else:
                continue
        return True
# @lc code=end

