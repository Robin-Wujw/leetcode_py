#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#

# @lc code=start
class Solution:
    #bfs
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge = [[] for _ in range(n)]
        for p, c in connections:
            edge[p].append((c, 1))
            edge[c].append((p, 0))
        quee = [0]
        vist = [False] * n
        vist[0] = True
        ans = 0
        while quee:
            i = quee.pop(0)
            print(i,edge[i])
            for n, c in edge[i]:
                if not vist[n]:
                    vist[n] = True
                    ans += c
                    quee.append(n)
        return ans
# @lc code=end

