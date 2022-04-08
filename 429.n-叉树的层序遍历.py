#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(root == None): return []
        q = Deque([root])
        results = []
        while(q):
            n = len(q)
            result = []
            for _ in range(n):
                cur = q.popleft()
                result.append(cur.val)
                for child in cur.children:
                    q.append(child)
            results.append(result)
        return results
        
# @lc code=end

