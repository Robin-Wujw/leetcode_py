#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root:TreeNode, targetSum):
        """    
        给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
        """
        def getDepth(root,sum):
            if(root.left==None and root.right==None and sum==targetSum):
                return True
            if(root.left==None and root.right==None):
                return False
            if(root.left):
                sum+=root.left.val
                if(getDepth(root.left,sum)):return True
                sum-=root.left.val
            if(root.right):
                sum+=root.right.val
                if(getDepth(root.right,sum)):return True
                sum-=root.right.val
        if(root==None):return False
        return getDepth(root,root.val)
def stringToTreeNode(input):
    input = input.strip()
    input = input[:]
    if not input:
        return None
    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root
if __name__ ==  "__main__":
    s = Solution()
    root =  "5,4,8,11,null,13,4,7,2,null,null,null,1"
    root = stringToTreeNode(root)
    targetsum = 22
    print(s.hasPathSum(root,targetsum))