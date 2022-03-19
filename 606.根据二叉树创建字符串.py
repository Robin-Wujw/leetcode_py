#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        result = str(root.val)
        if root.left:
            result += "(" + self.tree2str(root.left) + ")"
        else:
            result += "()"
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"
        return result
# @lc code=end

