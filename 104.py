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
        return self.getDepth(root)
    def getDepth(self,root):
        if not root: return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        depth =  1 + max(leftDepth,rightDepth)
        return depth

    #   迭代法
        # if not root:
        #     return 0
        # quene = [root]
        # depth = 0
        # while(quene):
        #     length = len(quene)
        #     depth += 1
        #     for _ in range(length):
        #         node = quene.pop(0)
        #         if node.left: quene.append(node.left)
        #         if node.right: quene.append(node.right)
        # return  depth
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
    tree = "3,9,20,null,null,15,7"
    tree = stringToTreeNode(tree)
    print(s.maxDepth(tree))

 