#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，检查它是否是镜像对称的。
        例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        """
        if not root:
            return True
        else:
            return self.compare(root,root)
    
    def compare(self,p,q):
            if not p and not q: return True
            elif not p or not q: return False
            elif p.val!= q.val: return False
            
            return self.compare(p.left,q.right) and self.compare(p.right,q.left)