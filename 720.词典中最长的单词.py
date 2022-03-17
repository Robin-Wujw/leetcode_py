#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (-len(x),x),reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word 
                candidates.add(word)
        return longest
# @lc code=end

