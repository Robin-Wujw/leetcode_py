# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if(root==None): return []
        queue = Deque([root])
        results = []
        while(queue):
            n = len(queue)
            for _ in range(n):
                cur = queue.popleft()
                results.append(cur.val)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
        return results

