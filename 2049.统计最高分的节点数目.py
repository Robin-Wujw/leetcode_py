#
# @lc app=leetcode.cn id=2049 lang=python3
#
# [2049] 统计最高分的节点数目
#

# @lc code=start
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0, 0
#dfs 中的 size 表示除了 node 为根节点的子树外，其他节点的数量。一开始假设 node 没有子节点，所以是 n - 1，遍历 node 子节点列表获取 node 左右子树的节点数量，size 要对应减少，遍历完后，剩余的 size，则是除了 node 为根的子树之外的其他节点数量。最后，score *= size，就求出了以这个节点为根结点的子树移除所形成的子树的分数，由于 root 节点的 size 一定为0，所以不能计算 root 节点。
        def dfs(node: int) -> int:
            score = 1
            size = n - 1 #表示除了 node 为根节点的子树外，其他节点的数量
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt
# @lc code=end

