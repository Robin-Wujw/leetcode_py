#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#
#深度遍历 加动态规划 因为在深度遍历时候,有重复子结构
# @lc code=start
from collections import defaultdict
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        print(graph)
        # {0: [1], 1: [2, 3], 7: [3], 3: [4, 5, 6]})
        n = len(quiet)
        res = [-1]*n
        
        def dfs(person):
            if res[person] >= 0:
                return res[person]
            res[person] = person
            for i in graph[person]:
                if quiet[res[person]] > quiet[dfs(i)]:
                    res[person] = res[i]
            return res[person]
        
        for person in range(n):
            dfs(person)
        return res
# @lc code=end

