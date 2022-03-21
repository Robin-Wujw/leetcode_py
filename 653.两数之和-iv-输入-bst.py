#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.s = set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if(root == None):
            return False
        if(k-root.val in self.s):
            return True
        self.s.add(root.val)
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)
# @lc code=end

