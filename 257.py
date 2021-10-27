class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
        叶子节点 是指没有子节点的节点。
        """
        result = []
        path = ''
        if(not root):
            return result 
        self.travel(root,path,result)
        return result
    def travel(self,root,path,result):
        path += str(root.val)
        cur = root 
        if(not cur.left and not cur.right):
            return result.append(path) 
        if(cur.left):
            self.travel(root.left,path+'->',result)
        if(cur.right):
            self.travel(root.right,path+'->',result)
        # else:
        #     path += '->'
        #     if(cur.left):
        #         self.travel(root.left,path,result)
        #     if(cur.right):
        #         self.travel(root.right,path,result)

    # class Solution:
    # def binaryTreePaths(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[str]
    #     """
    #     def construct_paths(root, path):
    #         if root:
    #             path += str(root.val)
    #             if not root.left and not root.right:  # 当前节点是叶子节点
    #                 paths.append(path)  # 把路径加入到答案中
    #             else:
    #                 path += '->'  # 当前节点不是叶子节点，继续递归遍历
    #                 construct_paths(root.left, path)
    #                 construct_paths(root.right, path)
    #     paths = []
    #     construct_paths(root, '')
    #     return paths