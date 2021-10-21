# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        """
        翻转一棵二叉树。
        """
        if(root==None):return None
        self.swap(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    def swap(self,root):
        root.left,root.right = root.right,root.left 
