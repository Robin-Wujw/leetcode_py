class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
        """
        result = 0
        def getDepth(self,root):
            if(root == None): return 0
            leftDepth = self.getDepth(root.left)
            if(leftDepth==-1): return -1
            rightDepth = self.getDepth(root.right)
            if(rightDepth==-1): return -1

        
            if(abs(leftDepth-rightDepth)>1):
                result = -1
            else:
                result =  1 + max(leftDepth,rightDepth)
            return result
        if(self.getDepth(root)==-1):
            return False
        else:
            return True