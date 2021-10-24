class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    """
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    """
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if(root.val == p.val or root.val == q.val):
        #     return root
        # if(root.val > p.val and root.val < q.val or root.val < p.val and root.val > q.val):
        #     return root 
        #有bug 只返回了一层递归输出，结果并不一定。
        # elif(root.val > p.val and root.val > q.val):
        #     self.lowestCommonAncestor(root.left,p,q)
        # elif(root.val < p.val and root.val < q.val):
        #     self.lowestCommonAncestor(root.right,p,q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root