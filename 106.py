class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        """
        根据一棵树的中序遍历与后序遍历构造二叉树。
        注意:
        你可以假设树中没有重复的元素。
        """
        # if not postorder: return None
        # root_val = postorder[-1]
        # root = TreeNode(root_val)

        # index = inorder.index(root_val)

        # inorder_left = inorder[0:index]
        # inorder_right = inorder[index+1:]

        # postorder_left = postorder[:len(inorder_left)]
        # print(postorder,postorder_left)
        # postorder_right = postorder[len(inorder_left):-1]
        # root.left = self.buildTree(inorder_left,postorder_left)
        # root.right = self.buildTree(inorder_right,postorder_right)
        # return root
        if not postorder: 
            return None

        # 第二步: 后序遍历的最后一个就是当前的中间节点. 
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点. 
        separator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边. 
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的. 
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root 
def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

if __name__ ==  "__main__":
    s = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = s.buildTree(inorder,postorder)
    print(treeNodeToString(root))