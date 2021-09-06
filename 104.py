# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    #     """
    #     给定一个二叉树，找出其最大深度。
    #     二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    #     说明: 叶子节点是指没有子节点的节点。
    #     """
    #     递归法
    #     return self.getDepth(root)
    # def getDepth(self,root):
    #     if not root: return 0
    #     leftDepth = self.getDepth(root.left)
    #     rightDepth = self.getDepth(root.right)
    #     depth =  1 + max(leftDepth,rightDepth)
    #     return depth

    #   迭代法
        if not root:
            return 0
        quene = [root]
        depth = 0
        while(quene):
            length = len(quene)
            depth += 1
            for _ in range(length):
                node = quene.pop(0)
                if node.left: quene.append(node.left)
                if node.right: quene.append(node.right)
        return  depth