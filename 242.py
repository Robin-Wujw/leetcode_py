class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
        注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
        示例 1:
        输入: s = "anagram", t = "nagaram"
        输出: true
        """
        result1 = {}
        for i in s:
            if(i not in result1):
                result1[i] = 1
            else:
                result1[i] += 1
        for i in t:
            if(i not in result1):
                return False
            else:
                result1[i] -= 1
        for i in result1.values():
            if(i!=0):
                return False
        return True