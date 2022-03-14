#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}
        for i,s in enumerate(list1):
            index[s] = i
        ans = []
        maxIndex = inf 
        for i,s in enumerate(list2):
            if(s in index):
                if(i + index[s] < maxIndex):
                    maxIndex = i + index[s]
                    ans = [s]
                elif(i + index[s] == maxIndex):
                    ans.append(s)
        return ans  
# @lc code=end

