class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode):
        """
        给定一个二叉树，找出其最小深度。
        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
        说明：叶子节点是指没有子节点的节点。
        """
        def getDepth(root):
            if(root==None):
                return 0
            leftDepth = getDepth(root.left)
            rightDepth = getDepth(root.right)
            if(root.left==None and root.right!=None):
                return 1 + rightDepth
            elif(root.left!=None and root.right==None):
                return 1 + leftDepth
            return 1 + min(leftDepth,rightDepth)
        return getDepth(root)
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
    root =  "3,9,20,null,null,15,7"
    root = stringToTreeNode(root)
    print(s.minDepth(root))