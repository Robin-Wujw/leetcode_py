#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        cur = head 
        dict= {}
        while cur:
            dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head 
        while cur:
            dict[cur].next = dict.get(cur.next)
            dict[cur].random = dict.get(cur.random)
            cur = cur.next 
        return dict[head]
            
        
# @lc code=end

