#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
        示例：
        二叉树：[3,9,20,null,null,15,7]
        返回其层序遍历结果：[[3],[9,20],[15,7]]
        """
        if not root:
            return []
        quene = [root]
        result = []

        while(quene):
            length = len(quene)
            in_list = []
            
            for _ in range(length):
                node = quene.pop(0)
                in_list.append(node.val)
                if node.left: quene.append(node.left)
                if node.right: quene.append(node.right)
            result.append(in_list)