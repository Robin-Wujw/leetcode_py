# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        sum = 0
        path = []
        ret  = []
        def recur(node,sum):
            if not node:
                return 
            sum += node.val
            path.append(node.val)
            if(not node.left and not node.right and sum==target):
                ret.append(path[:])

            recur(node.left,sum)
            recur(node.right,sum)
            path.pop()
        recur(root,sum)
        return ret 