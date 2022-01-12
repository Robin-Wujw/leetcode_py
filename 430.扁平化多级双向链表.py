#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        v = []
        def dfs(head):
            if(head==None):
                return
            v.append(head)
            dfs(head.child)
            dfs(head.next)
        dfs(head)
        n = len(v)
        for i in range(n):
            if(i+1<n):
                v[i].next = v[i+1]
            if(i>0):
                v[i].prev = v[i-1]
            v[i].child = None
        return head
        
# @lc code=end

