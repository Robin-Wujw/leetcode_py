#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict = {}
        for word in words:
            res = ""
            for i in word:
                res += Morse[ord(i)-ord('a')]
            if(res not in dict):
                dict[res] = word
        return len(dict)
# @lc code=end

