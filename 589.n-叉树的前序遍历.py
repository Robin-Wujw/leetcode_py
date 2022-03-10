#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # ans = []
        # def dfs(node: 'Node'):
        #     if node is None:
        #         return
        #     ans.append(node.val)
        #     for ch in node.children:
        #         dfs(ch)
        # dfs(root)
        # return ans

        if root is None:
            return []
        ans = []
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(reversed(node.children))
        return ans
# @lc code=end

