#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # dict = {}
        # for i in edges:
        #     for j in i:
        #         if(j not in dict):
        #             dict[j] = 1 
        #         else:
        #             dict[j] += 1 
        # for i in dict:
        #     if(dict[i]==len(edges)):
        #         return i 
        # if(edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]):
        #     return edges[0][0]
        # else:
        #     return edges[0][1]
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]
# @lc code=end

