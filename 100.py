#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        输入：p = [1,2,3], q = [1,2,3]
        输出：true
        """
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val != q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

def stringToTreeNode(input):
    input = input[1:-1]
    if not input:
        return None

    inputValues = input
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

def main():
    z = [1,2,3]
    x = [1,2,3]
    p = stringToTreeNode(z)
    q = stringToTreeNode(x)
    
    ret = Solution().isSameTree(p, q)

    out = (ret)
    print(out)

if __name__ == '__main__':
    main()