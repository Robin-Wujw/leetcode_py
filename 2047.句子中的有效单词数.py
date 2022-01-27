#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#

# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        # def valid(s: str) -> bool:
        #     hasHyphens = False
        #     for i, ch in enumerate(s):
        #         if ch.isdigit() or ch in "!.," and i < len(s) - 1:
        #             return False
        #         if ch == '-':
        #             if hasHyphens or i == 0 or i == len(s) - 1 or not s[i - 1].islower() or not s[i + 1].islower():
        #                 return False
        #             hasHyphens = True
        #     return True

        # return sum(valid(s) for s in sentence.split())
        arr = sentence.split()
        cnt = 0

        for word in arr:
            # 两种匹配模式，「 | 」 左边为有连接号的更长匹配，右边仅为单词与标点符号的匹配
            p = re.match(r'[a-z]+-?[a-z]+[!.,]?|[a-z]*[!.,]?', word)
            if p and p.group(0) == word:
                cnt += 1
        
        return cnt

# @lc code=end

