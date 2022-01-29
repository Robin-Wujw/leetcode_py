#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # dict = {}
        # res = []
        # list1 = s1.split(" ")
        # list2 = s2.split(" ")
        # for i in list1:
        #     if(i in dict):
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1 
        # for i in list2:
        #     if(i in dict):
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1
        # for i in dict:
        #     if(dict[i]==1):
        #         res.append(i)
        # return res
        freq = Counter(s1.split()) + Counter(s2.split())
        
        ans = list()
        for word, occ in freq.items():
            if occ == 1:
                ans.append(word)
        
        return ans
# @lc code=end

