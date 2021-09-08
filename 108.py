class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        """
        给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
        高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
        输入：nums = [-10,-3,0,5,9]
        输出：[0,-3,9,-10,null,5]
        解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
        """
        def buildTree(left,right):
            if left > right: return None
            mid = left + (right - left)//2
            val = nums[mid]
            root = TreeNode(val)
            root.left = buildTree(left,mid-1)
            root.right = buildTree(mid+1,right)
            return root 
        root = buildTree(0,len(nums)-1)
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
    nums =  [-10,-3,0,5,9]
    root = s.sortedArrayToBST(nums)
    print(treeNodeToString(root))
