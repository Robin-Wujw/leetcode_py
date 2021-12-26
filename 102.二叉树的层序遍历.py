#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None): return []
        q = Deque([root])
        results = []
        while(q):
            n = len(q)
            result = []
            for _ in range(n):
                cur = q.popleft()
                result.append(cur.val)
                if(cur.left):
                    q.append(cur.left)
                if(cur.right):
                    q.append(cur.right)
            results.append(result)
        return results
# @lc code=end

