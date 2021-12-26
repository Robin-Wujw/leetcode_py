#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        results = []
        text1 = text.split()
        print(text1)
        for i in range(1,len(text1)-1):
            if(text1[i-1]==first and text1[i]==second):
                results.append(text1[i+1])
        return results
# @lc code=end

