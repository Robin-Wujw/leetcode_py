class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。
        填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
        初始状态下，所有 next 指针都被设置为 NULL。
        输入：root = [1,2,3,4,5,6,7]
        输出：[1,#,2,3,#,4,5,6,7,#]
        解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
        """
        # def traversal(root):
        #     if(not root): return []
        #     if(root.left):
        #         root.left.next = root.right
        #     if(root.right):
        #         if(root.next):
        #             root.right.next = root.next.left
        #         else:
        #             root.right.next = None
        #     traversal(root.left)
        #     traversal(root.right)
        # traversal(root)
        # return root
        if not root:
            return []
        quene = [root]

        while(quene):
            length = len(quene)
            for _ in range(length):
                if(_==0):
                    nodePre = quene.pop(0)
                    node = nodePre
                else:
                    node = quene.pop(0)
                    nodePre.next = node 
                    nodePre = nodePre.next
                if node.left: quene.append(node.left)
                if node.right: quene.append(node.right)
            nodePre.next = None
        return root
               
