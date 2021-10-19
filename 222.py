# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
    完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
    """
    # def countNodes(self, root):
    #     return self.getNodes(root)
    # def getNodes(self,root):
    #     if(not root): return 0
    #     leftNum = self.getNodes(root.left)
    #     rightNum = self.getNodes(root.right)
    #     Num = leftNum + rightNum + 1 
    #     return Num 
    def countNodes(self,root):
        if(not root):
            return 0
        leftN = root.left 
        rightN = root.right
        leftHight = 0 
        rightHight = 0
        while(leftN):
            leftN = leftN.left
            leftHight +=1
        while(rightN):
            rightN = rightN.right
            rightHight +=1
        if(leftHight == rightHight):
            return (2 >> leftHight -1)
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 


