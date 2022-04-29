# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

from typing import Deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root==None): return None
        queue = Deque([root])
        results = []
        flag = True 
        while(queue):
            n = len(queue)
            result = []
            for _ in range(n):
                if(flag==True):
                    cur = queue.popleft()
                else:
                    cur = queue.pop()
                result.append(cur.val)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
            results.append(result)
            flag = not flag
        return results

