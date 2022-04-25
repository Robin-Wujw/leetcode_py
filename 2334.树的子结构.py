# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A,B):
            if(B==None): return True
            if(A==None): return False
            return A.val==B.val and recur(A.left,B.val) and recur(A.right,B.right)

        return bool(A and B) and (recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))