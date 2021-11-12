#
# @lc app=leetcode.cn id=404 lang=python3
# 计算给定二叉树的所有左叶子之和。
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     sum = 0
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         if (root == None): return 0
#         if not root.left and not root.right:
#             Solution.sum += root.val
#         if root.left:
#             self.sumOfLeftLeaves(root.left)
#         if root.right and  root.right.left:
#             self.sumOfLeftLeaves(root.right)
#         return Solution.sum
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right) # 右
        
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right: 
            cur_left_leaf_val = root.left.val 
            
        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum # 中
        
# @lc code=end

