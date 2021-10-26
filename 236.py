class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        """
        if(root == p or root == q or root == None):
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if(left!=None and right !=None):
            return root 
        elif(left==None and right!=None):
            return right
        elif(right==None and left!=None):
            return left 
        else:
            return None
        