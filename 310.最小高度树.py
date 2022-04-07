#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
class Solution:
# 1.首先，我们看了样例，发现这个树并不是二叉树，是多叉树。
# 2.然后，我们可能想到的解法是：根据题目的意思，就挨个节点遍历bfs，统计下每个节点的高度，然后用map存储起来，后面查询这个高度的集合里最小的就可以了。
# 但是这样会超时的。
# 3.于是我们看图（题目介绍里面的图）分析一下，发现，越是靠里面的节点越有可能是最小高度树。
# 所以，我们可以这样想，我们可以倒着来。
# 4.我们从边缘开始，先找到所有出度为1的节点，然后把所有出度为1的节点进队列，然后不断地bfs，最后找到的就是两边同时向中间靠近的节点，那么这个中间节点就相当于把整个距离二分了，那么它当然就是到两边距离最小的点啦，也就是到其他叶子节点最近的节点了。
# 然后，就可以写代码了。

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        if n==1:
            res.append(0)
            return res
        degree = [0]*n #记录每个点的度
        map = defaultdict(list) #存储邻居节点
        # 初始化每个节点的度和邻居
        for edge in edges:
            degree[edge[0]]+=1
            degree[edge[1]]+=1
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        
        # 记录度为1的叶子节点
        queue = deque()
        for i in range(n):
            if degree[i]==1:
                queue.append(i)
        
        #每次遍历叶子节点，每一轮将叶子节点从树上删除后将新的叶子节点入队进行下一轮遍历
        while len(queue)>0:
            res = []
            size = len(queue)
            # 遍历叶子节点
            for i in range(size):
                cur = queue.pop()
                res.append(cur)
                neighbors = map[cur]
                for neighbor in neighbors:
                    # 将叶子节点的邻居节点的度减一，若是新的叶子节点，则入队
                    degree[neighbor]-=1
                    if degree[neighbor]==1:
                        queue.appendleft(neighbor)
        # 返回最后一轮的叶子节点，就是最小高度树的根节点
        return res

# @lc code=end

 