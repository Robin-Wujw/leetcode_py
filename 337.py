
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
    输入: [3,2,3,null,3,null,1]
        3
        / \
        2   3
        \   \ 
        3   1
    输出: 7 
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
    """
    # memory = {}
    # def rob(self, root):
    #     if root == None:
    #         return 0
    #     if root.left == None and root.right == None:
    #         return root.val
    #     if self.memory.get(root) != None:
    #         return self.memory[root]
        
    #     val1 = root.val
    #     if root.left:
    #         val1 += self.rob(root.left.left) + self.rob(root.left.right)
    #     if root.right:
    #         val1 += self.rob(root.right.left) + self.rob(root.right.right)
        
    #     val2 = self.rob(root.left) + self.rob(root.right)
    #     self.memory[root] = max(val1, val2)
    #     return max(val1, val2)
    # 动态规划
    def rob(self, root):
        result = self.rob_tree(root)
        return max(result[0], result[1])
    
    def rob_tree(self, node):
        if node is None:
            return (0, 0) # (偷当前节点金额，不偷当前节点金额)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1] # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1]) # 不偷当前节点，可偷可不偷子节点
        return (val1, val2)
